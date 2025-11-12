from app import init_app
import uvicorn 


server = init_app() 

if __name__ == "__main__":
    server = init_app() 
    uvicorn.run(server, reload=True) 
