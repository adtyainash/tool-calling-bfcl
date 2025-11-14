from openai import OpenAI
import json

import httpx

class NoAuthTransport(httpx.Auth):
    def auth_flow(self, request):
        # Remove Authorization header if present
        request.headers.pop("authorization", None)
        yield request


# Change this to your model URL (e.g., your LiteLLM endpoint)
client = OpenAI(
    base_url="https://litellm-staging.gopay.sh",  # or your LiteLLM proxy URL
    api_key="test-key",  # arbitrary if your backend ignores it
    http_client=httpx.Client(auth=NoAuthTransport())
)

# Define a local tool (e.g. simple calculator)
def add_numbers(a, b):
    return {"result": a + b}

tools = [
    {
        "type": "function",
        "function": {
            "name": "add_numbers",
            "description": "Add two numbers together.",
            "parameters": {
                "type": "object",
                "properties": {
                    "a": {"type": "number"},
                    "b": {"type": "number"},
                },
                "required": ["a", "b"]
            },
        },
    },
]

# Step 1: Ask model to call tool
response = client.chat.completions.create(
    model="GoToCompany/Llama-Sahabat-AI-v2-70B-R",  # your model name
    messages=[
        {"role": "user", "content": "What is 42 plus 58? Use tool."}
    ],
    tools=tools,
    tool_choice="auto"
)

message = response.choices[0].message
print("Raw model output:\n", message)

# Step 2: If model requested a tool call, handle it
if hasattr(message, "tool_calls") and message.tool_calls:
    for tool_call in message.tool_calls:
        func_name = tool_call.function.name
        args = json.loads(tool_call.function.arguments)

        if func_name == "add_numbers":
            result = add_numbers(**args)

            # Step 3: Send result back to model
            follow_up = client.chat.completions.create(
                model="GoToCompany/Llama-Sahabat-AI-v2-70B-R",
                messages=[
                    {"role": "user", "content": "What is 42 plus 58?"},
                    message,  # original message with tool call
                    {
                        "role": "tool",
                        "tool_call_id": tool_call.id,
                        "content": json.dumps(result)
                    }
                ]
            )
            print("\nFinal answer:\n", follow_up.choices[0].message.content)
else:
    print("\nNo tool call made.")
