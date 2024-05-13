import os

class Config_Handler:
    def __init__(self, file: str = "config") -> None:
        self.path_to_file = os.path.join("config", file)
        with open(self.path_to_file, "r") as f:
            data = f.read()

        data_dict = {}
        for i in data.split("\n"):
            if i:
                k, v = i.split("=")
                data_dict.update({k:v})
        
        self.data_dict = data_dict

    def get_all_config(self) -> dict:

        return self.data_dict

    def get_config(self, key: str) -> str | None:
        try:
            return self.data_dict[key]
        except:
            return None


    def set_config(self, key: str, value: str) -> None:
        
        self.data_dict[key] = str(value)
        self.save_config()

    def save_config(self):
        
        data = ""
        
        for key, value in self.data_dict.items():
            data += key + "=" + value + "\n"
        
        with open(self.path_to_file, "w") as f:
            f.write(data)



if __name__ == "__main__":
    ch = Config_Handler()
    # ch.set_config("ABC", "")
    # print(ch.get_config("lol"))
    print(ch.get_all_config())
