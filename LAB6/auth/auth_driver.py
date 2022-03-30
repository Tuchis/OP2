import auth

# Set up a test user and permission
auth.authenticator.add_user("admin", "adminadmin")
auth.authorizor.add_permission("test program")
auth.authorizor.add_permission("change program")
auth.authorizor.add_permission("have notebook")
auth.authorizor.permit_user("test program", "admin")
auth.authorizor.permit_user("change program", "admin")


class Editor:
    def __init__(self):
        self.username = None
        self.menu_map = {
            "login": self.login,
            "sign": self.sign,
            "notes": self.notes,
            "test": self.test,
            "change": self.change,
            "quit": self.quit,
        }
        self.change_map = {
            "delete": self.delete,
            "add": self.add,
            "permit": self.permit,
            "quit": self.exit,
        }

    def login(self):
        logged_in = False
        while not logged_in:
            username = input("username: ")
            if username == "":
                break
            password = input("password: ")
            try:
                logged_in = auth.authenticator.login(username, password)
            except auth.InvalidUsername:
                print("Sorry, that username does not exist")
            except auth.InvalidPassword:
                print("Sorry, incorrect password")
            else:
                self.username = username

    def sign(self):
        username = input("New username: ")
        password = input("password: ")
        try:
            auth.authenticator.add_user(username, password)
            auth.authorizor.permit_user("have notebook", username)
        except auth.UsernameAlreadyExists:
            print("Sorry, that username is taken")
        except auth.PasswordTooShort:
            print("Sorry, too short password")

    def notes(self):
        if self.is_permitted("have notebook"):
            try:
                auth.authenticator.users[self.username].notebook.run()
            except GeneratorExit:
                pass
        else:
            print("You can't have the notebook")

    def is_permitted(self, permission):
        try:
            auth.authorizor.check_permission(permission, self.username)
        except auth.NotLoggedInError as e:
            print("{} is not logged in".format(e.username))
            return False
        except auth.NotPermittedError as e:
            print("{} cannot {}".format(e.username, permission))
            return False
        else:
            return True

    def test(self):
        if self.is_permitted("test program"):
            print("Testing program now...")
            print("Printing all notebooks of all users:")
            print("\n".join([user + "'s notebook: \n" + str(auth.authenticator.users[user].notebook.notebook) for user in auth.authenticator.users]))

    def change(self):
        if self.is_permitted("change program"):
            try:
                self.change_menu()
            except GeneratorExit:
                pass
            print("Changing program now...")

    def quit(self):
        raise SystemExit()

    def menu(self):
        try:
            answer = ""
            while True:
                slash = "\\"
                print(
                    f"""
{"You are loggen in as " + self.username + f"{chr(10)}" if self.username else ""}\
Please enter a command:
\tlogin\tLogin
\tsign\tSign up\
{f"{chr(10)}{chr(9)}notes{chr(9)}Open notebook" if self.username else ""}
\ttest\tTest the program
\tchange\tChange the program
\tquit\tQuit
"""
                )
                answer = input("enter a command: ").lower()
                try:
                    func = self.menu_map[answer]
                except KeyError:
                    print("{} is not a valid option".format(answer))
                else:
                    func()
        finally:
            print("Thank you for testing the auth module")

    def change_menu(self):
        try:
            answer = ""
            while True:
                print(
                    f"""
{"You are loggen in as " + self.username + f"{chr(10)}" if self.username else ""}\
Please enter a command:
\tdelete\tDelete user
\tadd\t\tAdd user
\tpermit\tAdd user permission
\tquit\tExit change menu
"""
                )
                answer = input("enter a command: ").lower()
                try:
                    func = self.change_map[answer]
                except KeyError:
                    print("{} is not a valid option".format(answer))
                except GeneratorExit:
                    break
                else:
                    func()
        finally:
            print("Exit change menu")

    def delete(self):
        username = input("Username: ")
        if username == self.username:
            print("You can't delete yourself")
        else:
            try:
                auth.authenticator.delete_user(username)
            except auth.UsernameNotExists:
                print("Sorry, that username doesn't exist")

    def add(self):
        username = input("New username: ")
        password = input("password: ")
        try:
            auth.authenticator.add_user(username, password)
        except auth.UsernameAlreadyExists:
            print("Sorry, that username is taken")
        except auth.PasswordTooShort:
            print("Sorry, too short password")

    def permit(self):
        username = input("Username: ")
        print(f"All available permisions: {', '.join(auth.authorizor.permissions)}")
        permission = input("What permission you want to give: ")
        try:
            auth.authorizor.permit_user(permission, username)
        except auth.PermissionError:
            print("Permission doesn't exist")
        except auth.InvalidUsername:
            print("Username doesn't exist")

    def exit(self):
        raise GeneratorExit

Editor().menu()
