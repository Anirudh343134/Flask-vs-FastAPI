from fastapi import FastAPI, Form, Request
import uvicorn
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

app = FastAPI()

templates = Jinja2Templates(directory="templates")


@app.get('/', response_class=HTMLResponse)
def home(request: Request):
    return templates.TemplateResponse("home.html", {"request": request})


@app.post('/', response_class=HTMLResponse)
def submit_form(request: Request, amount: str = Form(...)):
    amount = int(amount)
    if amount > 99999999999999 or amount <= 0:
        return templates.TemplateResponse("home.html", {"request": request})
    else:
        denominations = [500, 200, 100, 50, 20, 10, 5, 2, 1]
        change = {}
        for denomination in denominations:
            if amount >= denomination:
                count = amount // denomination
                amount = amount % denomination
                change[denomination] = count


    return templates.TemplateResponse('change.html', {"request": request, "notes": change})



if __name__ == "__main__":
    uvicorn.run(app)