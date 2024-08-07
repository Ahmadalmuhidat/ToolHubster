import json
import uuid
import customtkinter

from CTkMessagebox import CTkMessagebox

customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("dark-blue")

class Tool(customtkinter.CTk):
  def __init__(self):
    try:
      self.data = None
      self.tools_labels = []

      self.createMainWindow()

    except Exception as e:
      CTkMessagebox(title="Error", message="Something went wrong!!!", icon="cancel")
      print(e)
      pass

  def updateTable(self):
    try:
      self.loadTool()
      self.displayTools()

    except Exception as e:
      CTkMessagebox(title="Error", message="Something went wrong!!!", icon="cancel")
      print(e)
      pass

  def createMainWindow(self):
    try:
      self.app = customtkinter.CTk()
      self.app.geometry("1500x950")
      self.app.title("TOOLHUBSTER")

      self.createHomePage(self.app)

      self.app.mainloop()

    except Exception as e:
      CTkMessagebox(title="Error", message="Something went wrong!!!", icon="cancel")
      print(e)
      pass

  def saveTool(self):
    try:
      entry = {
        "id": str(uuid.uuid1())[:10],
        "name": self.tool_name_entry.get().strip(),
        "path/GitHub link":  self.tool_path_entry.get().strip(),
        "description": self.tool_description_entry.get("0.0", "end").strip(),
        "keywords": [keyword.strip().lower() for keyword in self.tool_keywords_entry.get(0.0, "end") .split(",")]
      }

      self.data.append(entry)
      json_data = json.dumps(self.data, indent=4)

      with open("Tools.json", "w") as json_file:
        json_file.write(json_data)

      self.updateTable()

      self.tool_name_entry.delete(0, customtkinter.END)
      self.tool_path_entry.delete(0, customtkinter.END)
      self.tool_description_entry.delete(0.0, "end")
      self.tool_keywords_entry.delete(0.0, "end")
    
    except Exception as e:
        CTkMessagebox(title="Error", message="Something went wrong!!!", icon="cancel")
        print(e)
        pass

  def InsertToolDialog(self):
    try:
      dialog = customtkinter.CTkToplevel(self.app)
      dialog.title("New Tool")
      dialog.geometry("600x350")
      dialog.resizable(width=0, height=0)

      content_frame = customtkinter.CTkFrame(dialog)
      content_frame.pack(padx=10, pady=10)

      tool_name_label = customtkinter.CTkLabel(content_frame, text="Tool Name:")
      tool_name_label.grid(row=0, column=0, padx=10, pady=5)
      self.tool_name_entry = customtkinter.CTkEntry(content_frame, width=300)
      self.tool_name_entry.grid(row=0, column=1, padx=10, pady=5)

      tool_path_label = customtkinter.CTkLabel(content_frame, text="Tool Path/GitHub link:")
      tool_path_label.grid(row=1, column=0, padx=10, pady=5)
      self.tool_path_entry = customtkinter.CTkEntry(content_frame, width=300)
      self.tool_path_entry.grid(row=1, column=1, padx=10, pady=5)

      tool_description_label = customtkinter.CTkLabel(content_frame, text="Tool Description:")
      tool_description_label.grid(row=2, column=0, padx=10, pady=5)
      self.tool_description_entry = customtkinter.CTkTextbox(content_frame, width=300, height=100)
      self.tool_description_entry.grid(row=2, column=1, padx=10, pady=5)

      tool_keywords_label = customtkinter.CTkLabel(content_frame, text="Tool Keywords (Comma Separated):")
      tool_keywords_label.grid(row=3, column=0, padx=10, pady=5)
      self.tool_keywords_entry = customtkinter.CTkTextbox(content_frame, width=300, height=100)
      self.tool_keywords_entry.grid(row=3, column=1, padx=10, pady=5)

      save_button = customtkinter.CTkButton(content_frame, text="Save", command=self.saveTool)
      save_button.grid(row=4, columnspan=2, sticky="nsew")

      dialog.lift()
      dialog.wait_window()

    except Exception as e:
        CTkMessagebox(title="Error", message="Something went wrong!!!", icon="cancel")
        print(e)
        pass

  def resetInputs(self):
    try:
      self.search_bar.delete(0, customtkinter.END)
      self.delete_bar.delete(0, customtkinter.END)

      self.search_bar.configure(placeholder_text="Search for tools by name or keywords")
      self.delete_bar.configure(placeholder_text="Tool ID")
      
      self.updateTable()

    except Exception as e:
      CTkMessagebox(title="Error", message="Something went wrong!!!", icon="cancel")
      print(e)
      pass     
   
  def createHomePage(self, parent):
      try:
        table_action_frame = customtkinter.CTkFrame(parent, bg_color="transparent")
        table_action_frame.pack(padx=10, fill="x", expand=False)

        search_button = customtkinter.CTkButton(table_action_frame, text="Search")
        search_button.grid(row=0, column=0, sticky="nsew", pady=10, padx=5)
        search_button.configure(command=lambda: self.searchTool(self.search_bar.get()))

        self.search_bar = customtkinter.CTkEntry(table_action_frame, width=450)
        self.search_bar.grid(row=0, column=1, sticky="nsew", pady=10)
        self.search_bar.configure(placeholder_text="Search for tools by name or keywords")

        delete_button = customtkinter.CTkButton(table_action_frame, width=100, text="Delete")
        delete_button.grid(row=0, column=2, sticky="nsew", pady=10, padx=5)
        delete_button.configure(command=lambda: self.deleteTool(self.delete_bar.get()))

        self.delete_bar = customtkinter.CTkEntry(table_action_frame, width=150)
        self.delete_bar.grid(row=0, column=3, sticky="nsew", pady=10)
        self.delete_bar.configure(placeholder_text="Tool ID")               

        reset_button = customtkinter.CTkButton(table_action_frame, width=100, text="Reset", command=self.resetInputs)
        reset_button.grid(row=0, column=4, sticky="nsew", pady=10, padx=5)

        add_new_tool_button = customtkinter.CTkButton(table_action_frame, width=100, text="Add New Tool", command=self.InsertToolDialog)
        add_new_tool_button.grid(row=0, column=5, sticky="nsew", pady=10, padx=5)

        self.tools_table_frame = customtkinter.CTkScrollableFrame(self.app)
        self.tools_table_frame.pack(padx=10, fill="both", expand=True)

        headers = ["Tool ID", "Tool Name", "Tool Path / GitHub link", "Tool Description"]

        for col, header in enumerate(headers):
          header_label = customtkinter.CTkLabel(self.tools_table_frame, text=header, padx=10, pady=20)
          header_label.grid(row=0, column=col, sticky="nsew")

        for col in range(len(headers)):
          self.tools_table_frame.columnconfigure(col, weight=1)

        self.updateTable()

      except Exception as e:
          CTkMessagebox(title="Error", message="Something went wrong!!!", icon="cancel")
          print(e)
          pass

  def displayTools(self):
    try:
      if len(self.tools_labels) > 0:
        for label in self.tools_labels:
          label.destroy()
        
      if len(self.data) > 0:
        for row, tool_data in enumerate(self.data):
          ToolID = tool_data.get("id", "N/A")
          ToolName = tool_data.get("name", "N/A")
          ToolPath = tool_data.get("path/GitHub link", "N/A")
          ToolDescription = tool_data.get("description", "N/A")

          ToolData = [ToolID, ToolName, ToolPath, ToolDescription]

          for col, data in enumerate(ToolData):
            data_label = customtkinter.CTkLabel(self.tools_table_frame, text=data, padx=10, pady=5)
            data_label.grid(row=row + 1, column=col, sticky="nsew")
            self.tools_labels.append(data_label)

    except Exception as e:
        CTkMessagebox(title="Error", message="Something went wrong!!!", icon="cancel")
        print(e)
        pass

  def loadTool(self):
    try:
      with open("Tools.json", 'r') as json_file:
        data = json.load(json_file)
        self.data = data

    except FileNotFoundError:
      errorMessage = CTkMessagebox(title="Error", message="Tools.json was not found", icon="cancel", option_1="close")
      data = None

      if errorMessage.get() == "close":
        exit()
    except Exception as e:
      CTkMessagebox(title="Error", message="Something went wrong!!!", icon="cancel")
      print(e)
      pass

  def deleteTool(self, id):
    try:
      with open("Tools.json", 'r') as json_file:
        data = json.load(json_file)

      new_data = [item for item in data if item["id"] != id]
      
      with open("Tools.json", 'w') as json_file:
        json.dump(new_data, json_file, indent=4)

      self.updateTable()

    except Exception as e:
      CTkMessagebox(title="Error", message="Something went wrong!!!", icon="cancel")
      print(e)
      pass

  def searchTool(self, term):
    try:
      with open("Tools.json", 'r') as json_file:
        data = json.load(json_file)
        results = []

      for item in data:
        if (item.get("name").lower() == term.lower()) or (term.lower() in item.get("keywords", [])) or (term.lower() in item.get("description", "").lower()):
          results.append(item)
          self.data = results
          self.displayTools()

    except Exception as e:
      CTkMessagebox(title="Error", message="Something went wrong!!!", icon="cancel")
      print(e)
      pass

if __name__ == "__main__":
  tool = Tool()