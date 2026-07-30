import sqlite3

conn = sqlite3.connect('youtube_video.db')

cursor = conn.cursor()

cursor.execute(''' 
    CREATE TABLE IF NOT EXISTS videos(
               id INTEGER PRIMARY KEY,
               name TEXT NOT NULL,
               time TEXT NOT NULL
               )
''')

def list_videos():
    cursor.execute("SELECT * FROM VIDEOS")
    for row in cursor.fetchall():
        print(row)

def add_video(name,time):
    cursor.execute("INSERT INTO VIDEOS (name,time) VALUES (?, ?)", (name,time))
    conn.commit()

def update_video(video_id,new_name,new_time):
    cursor.execute("UPDATE videos SET name = ?,time = ? WHERE ID = ?", (new_name,new_time,video_id))
    conn.commit()
    

def delete_video(video_id):
    cursor.execute("DELETE FROM videos WHERE id = ?",(video_id,))
    conn.commit()



def main():
    while True:
        print("\n Youtube manager app with DB")
        print("\n Youtube Manager | choose an option ")
        print("1. List all youtube videos ")
        print("2. Add a youtube video ")
        print("3. Update a youtube video details ")
        print("4. Delete a youtube video ")
        print("5. Exite the app ")
        choice = input("Entrer your choice: ")

        if choice == '1':
            list_videos()
        
        elif choice == '2':
            name = input("Enter the video name: ")
            time = input("Enter the video time: ")
            add_video(name,time)
        
        elif choice == '3':
            video_id = input("Enter the video ID to update: ")
            name = input("Enter the video name: ")
            time = input("Enter the video time: ")
            update_video(video_id,name,time)

        elif choice == '4':
            video_id = input("Enter the video ID to delete: ")
            delete_video(video_id)

        elif choice == '5':
            break
        else:
            print("Invalid choice ")
    conn.close()




if __name__ == "__main__":
    main()