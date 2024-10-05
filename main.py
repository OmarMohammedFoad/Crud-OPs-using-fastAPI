from fastapi import Body, FastAPI,HTTPException
from typing import List
from uuid import UUID,uuid4

from model import User,Genders,Role
app = FastAPI()
db:List[User]=[
    User(
        id=uuid4(),
        first_name="omar",
        last_name="Muhammad",
        middle_name="fouad",
        gender=Genders.male,
        role=[Role.admin]
    ),
       User(
        id=uuid4(),
        first_name="Abdullah",
        last_name="Yasser",
        middle_name="Anwar",
        gender=Genders.male,
        role=[Role.studnet]
    )
]



@app.get("/api/v1/users")
async def  fetch_users():
    return db



@app.get("/api/v1/user/{user_id}")
async def get_one_user(user_id: UUID):
    for user in db:
        if user.id == user_id:
            return user

# @app.get("/api/v1/users/:id")
# async def   fetch_one_user(id:str):
    
@app.post("/api/v1/users/")
async def create_user(user:User):
    db.append(user)
    return {"user":f"user{user.id}  has been created"}
    

@app.delete("/api/v1/users/{user_id}")
async def  delete_one_user(user_id:UUID):
    for user in db:
        if user.id == user_id:
            db.remove(user)
            return f"{user.first_name} has been deleted"
        raise HTTPException(
            status_code=404,
            detail=f"the user is not found"

        )
    
# BOOKS = [
#     {'title': 'Title One', 'author': 'Author One', 'category': 'science'},
#     {'title': 'Title Two', 'author': 'Author Two', 'category': 'science'},
#     {'title': 'Title Three', 'author': 'Author Three', 'category': 'history'},
#     {'title': 'Title Four', 'author': 'Author Four', 'category': 'math'},
#     {'title': 'Title Five', 'author': 'Author Five', 'category': 'math'},
#     {'title': 'Title Six', 'author': 'Author Two', 'category': 'math'}
# ]


# @app.get("/books")
# async def getAllBooks():
#     return BOOKS

# @app.get("/books/{title}")
# async def getOneBookAuthor(title:str):
#     for book in BOOKS:        
#         if  book.get('title').casefold() == title.casefold():
#             return book





# @app.get("/books/byauthor/")
# async def getBookByAuthor(author:str):
#     # for book in BOOKS:
#     #     if book.get('author').casefold() == author.casefold():
#     #         filteredBooksbyAuthor.append(book)
    
#     filteredBooksbyAuthor = [book for book in BOOKS if book.get('author').casefold() == author.casefold()]
#     print(len(filteredBooksbyAuthor))
#     if filteredBooksbyAuthor :
#         return filteredBooksbyAuthor
#     else:
#         return {"result": "not found"}
    

# @app.get("/books/categories/")
# async def  getBooksbyCategory(category:str):
#     print("")
#     filterBooksByCategories = [book for book in BOOKS if book.get('category').casefold()==category.casefold()]
#     if filterBooksByCategories:
#         return filterBooksByCategories
#     else:
#         return {"result":"not found"}
 
