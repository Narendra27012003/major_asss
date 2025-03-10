import os
from dotenv import load_dotenv
from srs_analysis import analyze_srs
from screenshot_analysis import analyze_screenshot

# Load environment variables from .env file
load_dotenv()

def main():
    # Update file paths to match the provided absolute paths
    srs_file_path = r"C:\Users\narebabu\Desktop\temp\SRD.docx"  # Path to the SRS document
    screenshot_file_path_1 = r"C:\Users\narebabu\Desktop\temp\pic1.png"  # Path to the first screenshot
    screenshot_file_path_2 = r"C:\Users\narebabu\Desktop\temp\pic2.png"  # Path to the second screenshot
    groq_api_key = os.getenv("GROQ_API_KEY")  # Get the API key from environment variables

    # Validate API key
    if not groq_api_key:
        print("Error: GROQ_API_KEY is not set in the .env file")
        return

    # Analyze the SRS document
    try:
        print("Analyzing SRS document...")
        srs_data = analyze_srs(srs_file_path)
        print("SRS Data Extracted:")
        print(srs_data)
    except Exception as e:
        print(f"Error analyzing SRS document: {e}")
        return

    # Analyze the first screenshot
    try:
        print("Analyzing Screenshot 1...")
        screenshot_data_1 = analyze_screenshot(screenshot_file_path_1, groq_api_key)
        print("Screenshot 1 Data Extracted:")
        print(screenshot_data_1)
    except Exception as e:
        print(f"Error analyzing Screenshot 1: {e}")

    # Analyze the second screenshot
    try:
        print("Analyzing Screenshot 2...")
        screenshot_data_2 = analyze_screenshot(screenshot_file_path_2, groq_api_key)
        print("Screenshot 2 Data Extracted:")
        print(screenshot_data_2)
    except Exception as e:
        print(f"Error analyzing Screenshot 2: {e}")

    # Combine data
    combined_data = {**srs_data, **screenshot_data_1, **screenshot_data_2}
    print("Combined Data:")
    print(combined_data)

if __name__ == "__main__":
    main()
