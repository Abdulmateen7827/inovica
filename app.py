# import streamlit as st
# import requests
# import base64
# import csv
# from io import StringIO
# import re

# # Function to encode an image from a URL to base64 format
# def encode_image_from_url(url):
#     response = requests.get(url)
#     if response.status_code == 200:
#         return base64.b64encode(response.content).decode('utf-8')
#     else:
#         return None

# # Function to send images to the model and get a comparison result
# def compare_images(base64_image1, base64_image2, model_name):
#     api_key = "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"
#     headers = {
#         "Content-Type": "application/json",
#         "Authorization": f"Bearer {api_key}"
#     }

#     payload = {
#         "model": model_name,
#         "messages": [
#             {
#                 "role": "user",
#                 "content": [
#                     {
#                         "type": "text",
#                         "text": "We want to do a three-way classification: match, not match, or partial match. \
#                         If both contain the same product, return 'Match'; if one contains a product that the other has \
#                         but has additional products alongside it, return 'Partial Match'; if the two products contain entirely \
#                         different products, return 'No Match'. Additionally, identify and return the type of product from each image \
#                         in the format 'Product Type: [TYPE]'. Format your response like this: 'Comparison Result: [RESULT]; Product 1 Type: [TYPE1]; Product 2 Type: [TYPE2]'."
#                     },
#                     {
#                         "type": "image_url",
#                         "image_url": {
#                             "url": f"data:image/jpeg;base64,{base64_image1}"
#                         }
#                     },
#                     {
#                         "type": "image_url",
#                         "image_url": {
#                             "url": f"data:image/jpeg;base64,{base64_image2}"
#                         }
#                     }
#                 ]
#             }
#         ],
#         "max_tokens": 3000
#     }

#     response = requests.post("https://api.openai.com/v1/chat/completions", headers=headers, json=payload)
#     response_json = response.json()

#     # Extracting the content from the response
#     content = response_json.get('choices', [{}])[0].get('message', {}).get('content', "")

#     # Using regex to parse the comparison result and product types
#     result_match = re.search(r'Comparison Result: (\w+)', content)
#     type1_match = re.search(r'Product 1 Type: (.+?);', content)
#     type2_match = re.search(r'Product 2 Type: (.+)', content)

#     comparison_result = result_match.group(1) if result_match else "Unknown"
#     product_type1 = type1_match.group(1) if type1_match else "Unknown"
#     product_type2 = type2_match.group(1) if type2_match else "Unknown"

#     return {
#         'comparison_result': comparison_result,
#         'product_type1': product_type1,
#         'product_type2': product_type2
#     }

# # Streamlit app
# st.title("Image Comparison and Classification")

# # Select GPT model
# model_name = st.selectbox(
#     "Select the GPT model to use",
#     ("gpt-4o-mini", "gpt-4o", "gpt-4", "gpt-3.5-turbo")
# )

# # Upload CSV file
# uploaded_file = st.file_uploader("Upload CSV file for testing", type=["csv"])

# if uploaded_file is not None:
#     # Specify number of rows to process
#     row_limit = st.number_input("Number of rows to process", min_value=1, max_value=100, value=10)

#     # Read the CSV file
#     csv_file = StringIO(uploaded_file.getvalue().decode("utf-8"))
#     reader = csv.reader(csv_file)
#     headers = next(reader)  # Skip the header row if present

#     results = [["Product Name", "Seller Name", "Image URL 1", "Image URL 2", "Product Type 1", "Product Type 2", "Comparison Result"]]  # Header for the output CSV

#     # Process the specified number of rows
#     for index, row in enumerate(reader):
#         if index >= row_limit:  # Stop processing after the specified number of rows
#             break

#         # Extract product name and image URLs from the specified columns
#         product_name = row[5]  # Column index 5 for product name
#         image_url1 = row[15]  # Column index 15
#         image_url2 = row[16]  # Column index 16
#         seller = row[7]

#         # Encode the images from URLs
#         base64_image1 = encode_image_from_url(image_url1)
#         base64_image2 = encode_image_from_url(image_url2)

#         # If images could not be fetched, log an error
#         if not base64_image1 or not base64_image2:
#             results.append([product_name, seller, image_url1, image_url2, "Error", "Error", "Error fetching images"])
#             continue

#         # Compare images using the model
#         comparison_result = compare_images(base64_image1, base64_image2, model_name)
        
#         results.append([
#             product_name,
#             seller,
#             image_url1,
#             image_url2,
#             comparison_result['product_type1'],
#             comparison_result['product_type2'],
#             comparison_result['comparison_result']
#         ])

#     # Display results in a table
#     st.write("Comparison Results:")
#     st.dataframe(results)

#     # Allow user to download the resulting CSV
#     output_csv = StringIO()
#     writer = csv.writer(output_csv)
#     writer.writerows(results)
#     st.download_button(
#         label="Download Comparison Results CSV",
#         data=output_csv.getvalue(),
#         file_name="comparison_results.csv",
#         mime="text/csv"
#     )

# import streamlit as st
# import requests
# import base64

# # Function to encode an image from a URL to base64 format
# def encode_image_from_url(url):
#     response = requests.get(url)
#     if response.status_code == 200:
#         return base64.b64encode(response.content).decode('utf-8')
#     else:
#         return None

# # Function to send images to the model and get a comparison result
# def compare_images(base64_image1, base64_image2, model_name):
#     api_key = "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"
#     headers = {
#         "Content-Type": "application/json",
#         "Authorization": f"Bearer {api_key}"
#     }

#     payload = {
#         "model": model_name,
#         "messages": [
#             {
#                 "role": "user",
#                 "content": [
#                     {
#                         "type": "text",
#                         "text": "We want to do a three-way classification: match, not match, or partial match. \
#                         If both contain the same product, return 'Match'; if one contains a product that the other has \
#                         but has additional products alongside it, return 'Partial Match'; if the two products contain entirely \
#                         different products, return 'No Match'."
#                     },
#                     {
#                         "type": "image_url",
#                         "image_url": {
#                             "url": f"data:image/jpeg;base64,{base64_image1}"
#                         }
#                     },
#                     {
#                         "type": "image_url",
#                         "image_url": {
#                             "url": f"data:image/jpeg;base64,{base64_image2}"
#                         }
#                     }
#                 ]
#             }
#         ],
#         "max_tokens": 3000
#     }

#     response = requests.post("https://api.openai.com/v1/chat/completions", headers=headers, json=payload)
#     response_json = response.json()

#     # Extracting the content from the response
#     content = response_json.get('choices', [{}])[0].get('message', {}).get('content', "")
#     return content

# # Streamlit app
# st.title("Image Comparison and Classification")

# # Select GPT model
# model_name = st.selectbox(
#     "Select the GPT model to use",
#     ("gpt-4o-mini", "gpt-4o", "gpt-4", "gpt-3.5-turbo")
# )

# # Input fields for image URLs
# image_url1 = st.text_input("Enter the first image URL")
# image_url2 = st.text_input("Enter the second image URL")

# if st.button("Compare Images"):
#     # Encode the images from URLs
#     base64_image1 = encode_image_from_url(image_url1)
#     base64_image2 = encode_image_from_url(image_url2)

#     # If images could not be fetched, show an error message
#     if not base64_image1 or not base64_image2:
#         st.error("Error fetching images. Please check the URLs.")
#     else:
#         # Compare images using the model
#         comparison_result = compare_images(base64_image1, base64_image2, model_name)
#         st.write("Comparison Result:")
#         st.write(comparison_result)

# import streamlit as st
# import requests
# import base64

# # Function to encode an image from a URL to base64 format
# def encode_image_from_url(url):
#     response = requests.get(url)
#     if response.status_code == 200:
#         return base64.b64encode(response.content).decode('utf-8')
#     else:
#         return None

# # Function to send images to the model and get a comparison result
# def compare_images(base64_image1, base64_image2, model_name):
#     api_key = "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"
#     headers = {
#         "Content-Type": "application/json",
#         "Authorization": f"Bearer {api_key}"
#     }

#     payload = {
#         "model": model_name,
#         "messages": [
#             {
#                 "role": "user",
#                 "content": [
#                     {
#                         "type": "text",
#                         "text": "We want to do a three-way classification: match, not match, or partial match. \
#                         If both contain the same product, return 'Match'; if one contains a product that the other has \
#                         but has additional products alongside it, return 'Partial Match'; if the two products contain entirely \
#                         different products, return 'No Match'. Additionally, identify and return the type of product from each image \
#                         in the format 'Product Type 1: [TYPE1]; Product Type 2: [TYPE2]; Comparison Result: [RESULT]'."
#                     },
#                     {
#                         "type": "image_url",
#                         "image_url": {
#                             "url": f"data:image/jpeg;base64,{base64_image1}"
#                         }
#                     },
#                     {
#                         "type": "image_url",
#                         "image_url": {
#                             "url": f"data:image/jpeg;base64,{base64_image2}"
#                         }
#                     }
#                 ]
#             }
#         ],
#         "max_tokens": 3000
#     }

#     response = requests.post("https://api.openai.com/v1/chat/completions", headers=headers, json=payload)
#     response_json = response.json()

#     # Extracting the content from the response
#     content = response_json.get('choices', [{}])[0].get('message', {}).get('content', "")

#     return content

# # Streamlit app
# st.title("Image Comparison and Classification")

# # Select GPT model
# model_name = st.selectbox(
#     "Select the GPT model to use",
#     ("gpt-4o-mini", "gpt-4o", "gpt-4", "gpt-3.5-turbo")
# )

# # Input for Image URLs
# image_url1 = st.text_input("Enter the URL of the first image")
# image_url2 = st.text_input("Enter the URL of the second image")

# # Compare Images button
# if st.button("Compare Images"):
#     if image_url1 and image_url2:
#         # Encode the images from URLs
#         base64_image1 = encode_image_from_url(image_url1)
#         base64_image2 = encode_image_from_url(image_url2)

#         # If images could not be fetched, display an error
#         if not base64_image1 or not base64_image2:
#             st.error("Error fetching images. Please check the URLs and try again.")
#         else:
#             # Compare images using the model
#             comparison_result = compare_images(base64_image1, base64_image2, model_name)
            
#             # Display the comparison result
#             st.write("Comparison Result:")
#             st.write(comparison_result)
#     else:
#         st.error("Please enter both image URLs before comparing.")

# import streamlit as st
# import requests
# import base64
# import re
# import pandas as pd
# import io

# # Function to encode an image from a URL to base64 format
# def encode_image_from_url(url):
#     response = requests.get(url)
#     if response.status_code == 200:
#         return base64.b64encode(response.content).decode('utf-8')
#     else:
#         return None

# # Function to send images to the model and get a comparison result
# def compare_images(base64_image1, base64_image2, model_name):
#     api_key = "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"
#     headers = {
#         "Content-Type": "application/json",
#         "Authorization": f"Bearer {api_key}"
#     }

#     payload = {
#         "model": model_name,
#         "messages": [
#             {
#                 "role": "user",
#                 "content": [
#                     {
#                         "type": "text",
#                         "text": "We want to do a three-way classification: match, not match, or partial match. \
#                         If both contain the same product, return 'Match'; if one contains a product that the other has \
#                         but has additional products alongside it, return 'Partial Match'; if the two products contain entirely \
#                         different products, return 'No Match'. Additionally, identify and return the type of product from each image \
#                         in the format 'Product Type 1: [TYPE1]; Product Type 2: [TYPE2]; Comparison Result: [RESULT]'."
#                     },
#                     {
#                         "type": "image_url",
#                         "image_url": {
#                             "url": f"data:image/jpeg;base64,{base64_image1}"
#                         }
#                     },
#                     {
#                         "type": "image_url",
#                         "image_url": {
#                             "url": f"data:image/jpeg;base64,{base64_image2}"
#                         }
#                     }
#                 ]
#             }
#         ],
#         "max_tokens": 3000
#     }

#     response = requests.post("https://api.openai.com/v1/chat/completions", headers=headers, json=payload)
#     response_json = response.json()

#     # Extracting the content from the response
#     content = response_json.get('choices', [{}])[0].get('message', {}).get('content', "")

#     return content

# # Function to parse the model output
# def parse_model_output(output):
#     pattern = r"Product Type 1: (.*?); Product Type 2: (.*?); Comparison Result: (.*)"
#     match = re.search(pattern, output)
#     if match:
#         return match.groups()
#     return None, None, None

# # Function to create DataFrame and CSV
# def create_dataframe_and_csv(data):
#     df = pd.DataFrame([data], columns=['Product Type 1', 'Product Type 2', 'Comparison Result'])
#     csv = df.to_csv(index=False)
#     return df, csv

# # Streamlit app
# st.title("Image Comparison and Classification")

# # Select GPT model
# model_name = st.selectbox(
#     "Select the GPT model to use",
#     ("gpt-4o-mini", "gpt-4o", "gpt-3.5-turbo")
# )

# # Input for Image URLs
# image_url1 = st.text_input("Enter the URL of the first image")
# image_url2 = st.text_input("Enter the URL of the second image")

# # Compare Images button
# if st.button("Compare Images"):
#     if image_url1 and image_url2:
#         # Encode the images from URLs
#         base64_image1 = encode_image_from_url(image_url1)
#         base64_image2 = encode_image_from_url(image_url2)

#         # If images could not be fetched, display an error
#         if not base64_image1 or not base64_image2:
#             st.error("Error fetching images. Please check the URLs and try again.")
#         else:
#             # Compare images using the model
#             comparison_result = compare_images(base64_image1, base64_image2, model_name)
            
#             # Parse the model output
#             product_type1, product_type2, result = parse_model_output(comparison_result)
            
#             if product_type1 and product_type2 and result:
#                 # Create DataFrame and CSV
#                 df, csv_data = create_dataframe_and_csv({
#                     'Product Type 1': product_type1, 
#                     'Product Type 2': product_type2, 
#                     'Comparison Result': result
#                 })
                
#                 # Display the result using st.dataframe
#                 st.write("Comparison Result:")
#                 st.dataframe(df, use_container_width=True)
                
#                 # Display the CSV
#                 # st.write("CSV format:")
#                 # st.code(csv_data, language='csv')
                
#                 # Provide download link for CSV
#                 st.download_button(
#                     label="Download CSV",
#                     data=csv_data,
#                     file_name="comparison_result.csv",
#                     mime="text/csv"
#                 )
#             else:
#                 st.error("Failed to parse the model output. Here's the raw output:")
#                 st.write(comparison_result)
#     else:
#         st.error("Please enter both image URLs before comparing.")

import streamlit as st
import requests
import base64
import re
import pandas as pd
import io

# Function to encode an image from a URL to base64 format
def encode_image_from_url(url):
    response = requests.get(url)
    if response.status_code == 200:
        return base64.b64encode(response.content).decode('utf-8')
    else:
        return None

# Function to send images to the model and get a comparison result
def compare_images(base64_image1, base64_image2, model_name):
    api_key = "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"
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {api_key}"
    }

    payload = {
        "model": model_name,
        "messages": [
            {
                "role": "user",
                "content": [
                    {
                        "type": "text",
                        "text": "We want to do a three-way classification: match, not match, or partial match. \
                        If both contain the same product, return 'Match'; if one contains a product that the other has \
                        but has additional products alongside it, return 'Partial Match'; if the two products contain entirely \
                        different products, return 'No Match'. Additionally, identify and return the type of product from each image \
                        in the format 'Product Type 1: [TYPE1]; Product Type 2: [TYPE2]; Comparison Result: [RESULT]'."
                    },
                    {
                        "type": "image_url",
                        "image_url": {
                            "url": f"data:image/jpeg;base64,{base64_image1}"
                        }
                    },
                    {
                        "type": "image_url",
                        "image_url": {
                            "url": f"data:image/jpeg;base64,{base64_image2}"
                        }
                    }
                ]
            }
        ],
        "max_tokens": 3000
    }

    response = requests.post("https://api.openai.com/v1/chat/completions", headers=headers, json=payload)
    response_json = response.json()

    # Extracting the content from the response
    content = response_json.get('choices', [{}])[0].get('message', {}).get('content', "")

    return content

# Function to parse the model output
def parse_model_output(output):
    pattern = r"Product Type 1: (.*?); Product Type 2: (.*?); Comparison Result: (.*)"
    match = re.search(pattern, output)
    if match:
        return match.groups()
    return None, None, None
# Function to create DataFrame and CSV
# def create_dataframe_and_csv(data):
#     df = pd.DataFrame([data], columns=['Product Type 1', 'Product Type 2', 'Comparison Result'])
#     csv = df.to_csv(index=False)
#     return df, csv

# Streamlit app
st.title("Image Comparison and Classification")

# Select GPT model
model_name = st.selectbox(
    "Select the GPT model to use",
    ("gpt-4o-mini", "gpt-4o", "gpt-3.5-turbo")
)

# Input for Image URLs
image_url1 = st.text_input("Enter the URL of the first image")
image_url2 = st.text_input("Enter the URL of the second image")

# Compare Images button
if st.button("Compare Images"):
    if image_url1 and image_url2:
        # Encode the images from URLs
        base64_image1 = encode_image_from_url(image_url1)
        base64_image2 = encode_image_from_url(image_url2)

        # If images could not be fetched, display an error
        if not base64_image1 or not base64_image2:
            st.error("Error fetching images. Please check the URLs and try again.")
        else:
            # Compare images using the model
            comparison_result = compare_images(base64_image1, base64_image2, model_name)
            
            # Parse the model output
            product_type1, product_type2, result = parse_model_output(comparison_result)
            
            if product_type1 and product_type2 and result:
                # Display the images and the comparison result in a table format
                st.markdown(f"""
                <table style='width:100%; border: 1px solid black; border-collapse: collapse;'>
                    <tr style='border: 1px solid black;'>
                        <th style='border: 1px solid black;'>Image 1</th>
                        <th style='border: 1px solid black;'>Image 2</th>
                        <th style='border: 1px solid black;'>Comparison Result</th>
                    </tr>
                    <tr style='border: 1px solid black;'>
                        <td style='border: 1px solid black;'>
                            <img src="{image_url1}" alt="Image 1" width="150" height="150">
                            <p>Product Type 1: {product_type1}</p>
                        </td>
                        <td style='border: 1px solid black;'>
                            <img src="{image_url2}" alt="Image 2" width="150" height="150">
                            <p>Product Type 2: {product_type2}</p>
                        </td>
                        <td style='border: 1px solid black;'>{result}</td>
                    </tr>
                </table>
                """, unsafe_allow_html=True)

                # # Create DataFrame and CSV
                # df, csv_data = create_dataframe_and_csv({
                #     'Product Type 1': product_type1, 
                #     'Product Type 2': product_type2, 
                #     'Comparison Result': result
                # })
                
            #     # Provide download link for CSV
            #     st.download_button(
            #         label="Download CSV",
            #         data=csv_data,
            #         file_name="comparison_result.csv",
            #         mime="text/csv"
            #     )
            # else:
            #     st.error("Failed to parse the model output. Here's the raw output:")
            #     st.write(comparison_result)
    else:
        st.error("Please enter both image URLs before comparing.")
