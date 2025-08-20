# Reads from input.txt and writes uppercase content to output.txt
def modify_file(input_filename, output_filename):
    print("🔍 Starting file modification...")

    try:
        # Step 1: Read input file
        with open(input_filename, 'r') as infile:
            content = infile.read()
            print("📄 Original content:", content)

        # Step 2: Modify content
        modified_content = content.upper()
        print("🔠 Modified content:", modified_content)

        # Step 3: Write to output file
        with open(output_filename, 'w') as outfile:
            outfile.write(modified_content)
        print(f"✅ Modified content written to {output_filename}")

    except FileNotFoundError:
        print(f"⚠️ Error: '{input_filename}' not found.")
    except Exception as e:
        print(f"❌ Unexpected error: {e}")

# Call the function
modify_file('input.txt', 'output.txt')