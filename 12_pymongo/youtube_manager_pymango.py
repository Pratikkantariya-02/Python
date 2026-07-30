import pymongo

client = pymongo.MongoClient("mongodb+srv://youtubepy:pratik2005@cluster0.4go3dpn.mongodb.net/",tlsAllowInvalidCertificates=True)

db = client["ytmanager"]
video_collection = db["videos"]

print(video_collection)

def add_video(name, time):
    video_collection.insert_one({"name": name, "time": time})

def list_videos():
    for video in video_collection.find():
        print(f"ID: {video['_id']}, Name: {video['name']}, Time: {video['time']}")

def update_video(video_id, name, time):
    video_collection.update_one({"_id":video_id},{"$set":{"name": name, "time": time}})

def delete_video(video_id):
    video_collection.delete_one({"_id":video_id})


def main():
    while True:
        print("\n Youtube manager App")
        print("1. List all videos")
        print("2. Add Video")
        print("3. Update Video")
        print("4. Delete Video")
        print("5. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            list_videos()
        elif choice == "2":
            name = input("Enter video name: ")
            time = input("Enter video time: ")
            add_video(name, time)
        elif choice == "3":
            video_id = input("Enter video ID to update: ")
            name = input("Enter video name to update: ")
            time = input("Enter new video time: ")
            update_video(video_id,name, time)
        elif choice == "4":
            video_id = input("Enter video ID to update: ")
            delete_video(video_id)
        elif choice == "5":
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()