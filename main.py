from fastapi import FastAPI
import os
from dotenv import load_dotenv

from models import TicketCreate, Ticket
from services import AIservice
load_dotenv()

# if os.getenv()

aiservice=AIservice()

ticket_db=[]
app = FastAPI(title="AI APP")

@app.get("/health")
def health():
    return {"msg":"Backend is running"}

@app.post("/tickets")
def tickets(ticket: TicketCreate):
    tickets_id = len(ticket_db) + 1
    prompt=f"""
you are a support agent, given a problem by user you should answer it 
politely, clearly and consisely.

user query:
title: {ticket.title}
description: {ticket.description}

"""
    response=aiservice.generate_reply(prompt)
    new_ticket=Ticket(
        title=ticket.title,
        description=ticket.description,
        id=tickets_id,
        ai_reply=response)
    ticket_db.append(new_ticket)
    return {
        "msg":"Ticket created succesfully",
        "ticket": new_ticket
    }


@app.get("/tickets")
def tickets():
    return ticket_db