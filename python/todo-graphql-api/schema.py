from typing import List 

from graphene import ObjectType, Field, String, ID, Int 
from graphene_sqlalchemy import SQLAlchemyObjectType

from database import get_db
from models import  Todo as TodoModel

class Todo(SQLAlchemyObjectType):
    class Meta: 
        model  = TodoModel
        interfaces = (ObjectType,) 

class Query(ObjectType):
    todos = Field(lambda: List[Todo], limit=Int())

    def resolve_todos(self, info, limit=None):
        query = Todo.get_query(info)
        if limit:
            return query.limit(limit).all()
        return query.all()

class CreateTodo(ObjectType):
    todo = Field(lambda: Todo)

    class Arguments:
        title = String(required=True)
        description = String()

    def mutate(self, info, title, decription):
        db = get_db()
        todo = TodoModel(title=title, description=description)
        db.add(todo)
        db.commit()
        db.refresh(todo)
        return CreateTodo(todo=todo)

class UpdateTodo(ObjectType):
    todo = Field(lambda: Todo)

    class Arguments:
        id = ID(required=True)
        title =  String()
        description = String()

    def mutate(self, info, id, title=None, description=None):
        db = get_db()
        todo = db.query(TodoModel).filter(TodoModel.id  == id).first()
        if not todo:
            raise Exception("Todo not found")
        if title:
            todo.title = title
        if decription: 
            todo.description = description
        db.commit()
        db.refresh(todo)
        return UpdateTodo(todo=todo)

class DeleteTodo(ObjectType):
    success = Field(lambda: String)

    class Arguments:
        id = ID(required=True)

    def mutate(self, info, id):
        db = get_db()
        todo = db.query(TodoModel).filter(TodoModel.id  == id).first()
        if not todo:
            raise Exception("Todo not found")
        db.delete(todo)
        db.commit()
        return DeleteTodo(success=f"Todo {id} delete successfully")

