from db_connection import *

if __name__ == '__main__':

    # Connecting to the database
    conn = connectDataBase()
    cur = conn.cursor()

    # Creating the tables (The database should be created manually)
    createTables(cur, conn)

    #print a menu
    print("")
    print("######### Menu ##############")
    print("#a - Create users and message")
    print("#b - Update a user")
    print("#c - Update a comment")
    print("#d - Delete a user and his/her comments")
    print("#e - Delete a comment")
    print("#f - Return a user")
    print("#g - Return the chat")
    print("#q - Quit")

    option = ""
    while option != "q":

          print("")
          option = input("Enter a menu choice: ")

          if (option == "a"):

              users = input("Enter the number os users: ")

              commentId = 0
              for u in range(int(users)):
                  userId = input("Enter the ID of user " + str(u + 1) + ": ")
                  userName = input("Enter the name of user " + str(u + 1) + ": ")
                  userEmail = input("Enter the email of user " + str(u + 1) + ": ")
                  createUser(cur, userId, userName, userEmail)
                  conn.commit()

                  comments = input("Enter the number of comments of user " + userName + ": ")
                  for c in range(int(comments)):
                      commentId += 1
                      commentText = input("Enter the text of " + userName + "'s " + str(c + 1) + " comment: ")
                      commentDate = input("Enter the date of " + userName + "'s " + str(c + 1) + " comment: ")
                      createComment(cur, commentId, userId, commentText, commentDate)

                  conn.commit()

          elif (option == "b"):

              userId = input("Enter the user id to be updated: ")
              userName = input("Enter the new name of user " + userId + ": ")
              userEmail = input("Enter the new email of user " + userId + ": ")

              updateUser(cur, userId, userName, userEmail)

              conn.commit()

          elif (option == "c"):

              commentId = input("Enter the comment id to be updated: ")
              commentText = input("Enter the new text of comment " + commentId + ": ")
              commentDate = input("Enter the new date of comment " + commentId + ": ")

              updateComment(cur, commentId, commentText, commentDate)

              conn.commit()

          elif (option == "d"):

              userId = input("Enter the user id to be deleted: ")

              deleteUser(cur, userId)

              conn.commit()

          elif (option == "e"):

              commentId = input("Enter the comment id to be deleted: ")

              deleteComment(cur, commentId)

              conn.commit()

          elif (option == "f"):

              nameUser = input("Enter the name of the user to be returned:  ")

              print(getUser(cur, nameUser))

              conn.commit()

          elif (option == "g"):

              print(getChat(cur))

              conn.commit()

          elif (option == "q"):

               print("Leaving the application ... ")

          else:

               print("Invalid Choice.")




