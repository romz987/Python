import pickle


class MusicBands:


    music_bands_dict = {
        "ac/dc": "thunderstruck",
        "metallica": "master of puppets",
        "iron maiden": "phantom of the opera",
        "sepultura": "attitude",
        "marilyn manson": "sacrilegious"
    }


    def __init__(self):
        pass 


    def add_data(self, band_name: str, song_name: str) -> str:
        self.music_bands_dict[band_name] = song_name
        return (f"'{band_name}: {song_name}' added")


    def search_data(self, name: str) -> str:
        for key, value in self.music_bands_dict.items():
            if key == name:
                return value
            if value == name:
                return key 
        return "searched data is not exists"
    

    def remove_data(self, name: str) -> str:
        for key, value in self.music_bands_dict.items():
            if key == name or value == name:
                self.music_bands_dict.pop(key)
                return (f"pair '{key}: {value}' deleted")


    def edit_data(self, data: str, new_data: str) -> str:
        for key, value in self.music_bands_dict.items():
            if key == data:
                self.music_bands_dict[new_data] = self.music_bands_dict.pop(key)
                return f"key changed from {key} to {new_data}"
            if value == data:
                self.music_bands_dict[key] = new_data
                return f"value changed from {value} to {new_data}"
        return "searched data is not exists"


    def pickle_data(self):
        try:
            with open("pickled_data_bands.pkl", "wb") as file:
                pickle.dump(self.music_bands_dict, file)
        except Exception as e:
            print(f"error: {str(e)}")
        else:
            return "data pickled"


    def load_data(self):
        try:
            with open("pickled_data_bands.pkl", "rb") as file:
                data = pickle.load(file)
                self.music_bands_dict = data
        except Exception as e:
            print(f"error: {str(e)}")
        else:
            return "data loaded"


if __name__ == "__main__":
    wmusic = MusicBands() 

    print(wmusic.add_data("stas piekha", "bez tebya"))
    print(wmusic.search_data("marilyn manson"))
    print(wmusic.remove_data("sepultura"))
    print(wmusic.edit_data("ac/dc", "AC/DC"))
    print(wmusic.music_bands_dict)

    wmusic.pickle_data()

    wmusic.load_data()

    print(wmusic.music_bands_dict)

