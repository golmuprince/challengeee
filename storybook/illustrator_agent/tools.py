import base64
from google.genai import types
from openai import OpenAI
from google.adk.tools.tool_context import ToolContext

client = OpenAI()

async def generate_images(tool_context: ToolContext):
    
    story_writer_output = tool_context.state.get("story_writer_output")
    
    if isinstance(story_writer_output, str):
        import json
        story_writer_output = json.loads(story_writer_output)

    pages = story_writer_output.get("pages")
    
    existing_artifacts = await tool_context.list_artifacts()
    
    STYLE_SUFFIX = (
        "watercolor illustration, soft pastel colors, "
        "children's picture book style, gentle and whimsical, "
        "no text, no letters"
    )

    results = []

    for page in pages:
        page_no = page.get("page_no")
        visual_desc = page.get("visual_desc")
        filename = f"page_{page_no}.jpeg"

        if filename not in existing_artifacts:
            full_prompt = f"{visual_desc}, {STYLE_SUFFIX}"
            image = client.images.generate(
                model="gpt-image-1",
                prompt=full_prompt,
                n=1,
                quality="low",
                moderation="low",
                output_format="jpeg",
                background="opaque",
                size="1024x1024",
            )
            image_bytes = base64.b64decode(image.data[0].b64_json)
            artifact = types.Part(
                inline_data=types.Blob(
                    mime_type="image/jpeg",
                    data=image_bytes,
                )
            )
            await tool_context.save_artifact(filename=filename, artifact=artifact)

        results.append({
            "page_no": page_no,
            "text": page.get("text"),
            "visual_desc": visual_desc,
            "filename": filename,
        })

    summary_lines = ["=== 동화가 완성되었습니다! ===\n"]
    for r in results:
        summary_lines.append(f"Page {r['page_no']}:\n")
        summary_lines.append(f"  Text: {r['text']}\n")
        summary_lines.append(f"  Visual: {r['visual_desc']}\n")
        summary_lines.append(f"  Image: [Artifact: {r['filename']}]\n")

    return {
        "status": "complete",
        "summary": "\n".join(summary_lines),
    }