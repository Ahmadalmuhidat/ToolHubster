# ToolHubster

## Overview
ToolHubster is a graphical user interface designed to manage a list of tools stored in a JSON-based database file. It allows users to add new tools, view existing tools, search for specific tools by name or keywords, and delete tools from the database.

## Dependencies
- `json`: Handles JSON file operations.
- `uuid`: Generates unique identifiers for tools.
- `customtkinter`: A custom Tkinter library used for creating the graphical interface.

## Features
- **Add New Tool:** Users can input details such as tool name, path/GitHub link, description, and keywords to add a new tool to the database.
- **View Tool List:** Displays a list of tools with columns for Tool ID, Name, Path/GitHub Link, and Description.
- **Search Functionality:** Enables searching for tools by name or keywords to find specific entries.
- **Delete Tools:** Allows the deletion of tools from the database using their unique Tool ID.

## Usage
1. **Installation:**
   - Ensure the necessary dependencies (`json`, `uuid`, `customtkinter`) are installed in your Python environment.

2. **Run ToolHubster:**
   - Execute the Python script containing the code for the ToolHubster tool manager GUI.

3. **Functionality:**
   - **Add New Tool:** Click on the "Add New Tool" button to input details for a new tool and save it to the database.
   - **View Tool List:** Displays the existing tools in the table format with their respective details.
   - **Search for Tools:** Use the search bar to find tools by name or keywords.
   - **Delete Tool:** Enter the Tool ID in the designated field and click the "Delete" button to remove the tool from the database.

## File Structure
- `Tools.json`: The JSON-based database file storing information about tools.

## Usage Notes
- Ensure the `Tools.json` file is present in the same directory as the Python script.
- When adding a new tool, fill in all required details (Tool Name, Path/GitHub link, Description, Keywords).
- Deletion requires entering the Tool ID, which is unique to each tool.

## Contributors
- Ahmad Almuhidat

## Support
For any issues, suggestions, or inquiries, feel free to contact ahmad.almuhidat@gmail.com.

