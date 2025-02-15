import json

def load_data():
    try:
        with open("youtube.tex", "r") as file:
            test = json.load(file)
            return test
    except FileNotFoundError:  
        return []   

def save_data_helper(videos):
    with open("youtube.tex", "w") as file:
        json.dump(videos, file)

def list_all_videos(videos):
    print("\n")
    print("*-*"*7)
    for index, video in enumerate(videos, start=1):  
        print(f"{index}. {video['name']} - {video['time']}")
    print("\n")
    print("*-*"*7)

def add_videos(videos):
    name = input("Enter the video name: ")
    time = input("Enter Video time: ")
    videos.append({"name": name, "time": time})
    save_data_helper(videos)

def update_videos(videos):
    list_all_videos(videos)
    index = int(input("Enter the vedeo number to update"))
    if 1 <= index <= len(videos):
        name = input("Enter the new video name")
        time = input("Enter the new video time")
        videos[index-1] = {"name":name ,"time": time}
        save_data_helper(videos)
    else:
        print("Invalid index selected")

def delete_videos(videos):
    list_all_videos(videos)
    index = int(input("Enter the vedio number to be deleted"))

    if 1 <= index <= len(videos):
        del videos[index -1]
        save_data_helper(videos)
    else:
        print("Invalide video selected")

def main():
    videos = load_data()
    while True:
        print("\nYoutube Manager | Choose your option")
        print("1. List of Favorite videos")
        print("2. Add a Youtube video")
        print("3. Update a Youtube video")
        print("4. Delete a Youtube video")
        print("5. Exit the app")

        choice = input("Enter your choice: ")
        
        match choice:
            case "1":
                list_all_videos(videos)
            case "2":
                add_videos(videos)
            case "3":
                update_videos(videos)
            case "4":
                delete_videos(videos)
            case "5":
                break
            case _:
                print("Invalid choice")

if __name__ == "__main__":
    main()
