import mysql.connector
import jdatetime 

db = mysql.connector.connect(
    host="localhost",
    username="root",
    password="",
    database="python-game"
)


class server:
    @staticmethod
    def isGroupExist(groupID):
        cursor = db.cursor()
        cursor.execute(f"SELECT * FROM `groups` WHERE `chatID` = '{groupID}' LIMIT 1")

        fetch = cursor.fetchall()

        if (len(fetch) > 0):
            return True 
        return False
    
    def createNewChat(groupID, title,telegramID):
        cursor = db.cursor()
        fa_date = jdatetime.date.today()
        fa_date.j_months_fa[0]
        date = jdatetime.datetime.now().strftime("%Y/%m/%d")
        modify_date = jdatetime.datetime.now().strftime("%Y/%m/%d %H:%M:%S")
        
        cursor.execute("INSERT INTO `groups` (`groupTitle`, `chatID`, `create_date`, `lastModify`, `ownerID`) VALUES (%s, %s, %s, %s, %s)", (title, groupID, date, modify_date, telegramID))
        db.commit()

    def isFactionOwner(telegramID, chatID):
        cursor = db.cursor()
        cursor.execute(f"SELECT * FROM `groups` WHERE `ownerID` = '{telegramID}' AND `chatID` = '{chatID}' LIMIT 1")

        fetch = cursor.fetchall()

        if (len(fetch) > 0):
            return True
        return False
    def isArmyExist(chatID):
        cursor = db.cursor()
        cursor.execute(f"SELECT * FROM `army` WHERE `chatID` = '{chatID}' LIMIT 1")

        fetch = cursor.fetchall()

        if (len(fetch) > 0):
            return True 
        return False
    def createNewArmy(chatID):
        cursor = db.cursor()
        cursor.execute(f"INSERT INTO `army` (`chatID`) VALUES ('{chatID}')")
        db.commit()
    def getArmyInformation(chatID):
        cursor = db.cursor()
        cursor.execute(f"SELECT * FROM `army` WHERE `chatID` = '{chatID}' LIMIT 1")

        fetch = cursor.fetchone()

        return fetch