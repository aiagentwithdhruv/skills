import os
import sys
import json
import time
import requests

def run():
    if len(sys.argv) < 3:
        print("Usage: python generate_kie.py <prompt_json_file> <output_file> [aspect_ratio]")
        sys.exit(1)
        
    prompt_file = sys.argv[1]
    output_file = sys.argv[2]
    aspect_ratio = sys.argv[3] if len(sys.argv) > 3 else "auto"
    
    env_path = os.path.join(os.path.dirname(__file__), '..', '.env')
    if not os.path.exists(env_path):
        print(f"ERROR: .env not found at {env_path}")
        sys.exit(1)
        
    api_key = None
    with open(env_path, 'r') as f:
        for line in f:
            if line.startswith('KIE_API_KEY='):
                api_key = line.strip().split('=', 1)[1].strip('"\'')
                break
                
    if not api_key:
        print("ERROR: KIE_API_KEY not found in .env")
        sys.exit(1)
        
    with open(prompt_file, 'r', encoding='utf-8') as f:
        prompt_json = json.load(f)
        
    image_input = prompt_json.pop("image_input", None)
    api_parameters = prompt_json.pop("api_parameters", {})
    
    prompt_string = json.dumps(prompt_json)
    
    url = "https://api.kie.ai/api/v1/jobs/createTask"
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {api_key}"
    }
    
    payload = {
        "model": "nano-banana-2",
        "input": {
            "prompt": prompt_string,
            "aspect_ratio": api_parameters.get("aspect_ratio", aspect_ratio),
            "resolution": api_parameters.get("resolution", "1K"),
            "output_format": api_parameters.get("output_format", "jpg")
        }
    }
    
    if "google_search" in api_parameters:
        payload["input"]["google_search"] = api_parameters["google_search"]
        
    if image_input:
        payload["input"]["image_input"] = image_input
    
    print("Creating task via Kie.ai API...")
    try:
        response = requests.post(url, headers=headers, json=payload, timeout=30)
        response.raise_for_status()
        result = response.json()
    except Exception as e:
        print(f"ERROR creating task: {e}")
        if 'response' in locals() and response is not None:
            print(response.text)
        sys.exit(1)
        
    task_id = result.get("data", {}).get("taskId")
    if not task_id:
        print("ERROR: No taskId returned")
        print(result)
        sys.exit(1)
        
    print(f"Task created successfully. Task ID: {task_id}. Polling...")
    
    poll_url = "https://api.kie.ai/api/v1/jobs/recordInfo"
    poll_params = {"taskId": task_id}
    
    attempts = 0
    while attempts < 60:
        time.sleep(4)
        attempts += 1
        
        try:
            poll_resp = requests.get(poll_url, headers=headers, params=poll_params, timeout=15)
            poll_resp.raise_for_status()
            poll_result = poll_resp.json()
        except Exception as e:
            print(f"Poll {attempts} Error: {e}")
            continue
            
        data = poll_result.get("data", {})
        if not data:
            print(f"Poll {attempts}: Received empty data object. Retrying...")
            continue
            
        state = data.get("state")
        print(f"Poll {attempts}: state = {state}")
        
        if state == "success" or state == "completed":
            result_json_str = data.get("resultJson", "{}")
            try:
                result_json = json.loads(result_json_str)
            except json.JSONDecodeError:
                result_json = {}
                
            result_urls = result_json.get("resultUrls", [])
            if result_urls and len(result_urls) > 0:
                image_url = result_urls[0]
                print(f"Downloading image from {image_url}")
                try:
                    img_resp = requests.get(image_url, timeout=30)
                    img_resp.raise_for_status()
                    with open(output_file, 'wb') as f:
                        f.write(img_resp.content)
                    print(f"Successfully saved to {output_file}")
                    sys.exit(0)
                except Exception as e:
                    print(f"ERROR downloading image: {e}")
                    sys.exit(1)
            else:
                print("ERROR: Could not find image URL in resultJson. Dumping data:")
                print(json.dumps(data, indent=2))
                sys.exit(1)
                
        elif state == "failed" or state == "error":
            print("ERROR: Task failed on server side.")
            print(json.dumps(data, indent=2))
            sys.exit(1)
            
    print("ERROR: Timed out waiting for job completion")
    sys.exit(1)

if __name__ == "__main__":
    run()
