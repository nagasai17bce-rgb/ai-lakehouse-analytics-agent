from fastapi import FastAPI,HTTPException
from pydantic import BaseModel,Field
from .db import connect
from .agent import AnalyticsAgent
app=FastAPI(title='AI Lakehouse Analytics Agent',version='0.1.0'); agent=AnalyticsAgent(connect())
class AnalyzeRequest(BaseModel): question:str=Field(min_length=3,max_length=500)
@app.get('/health')
def health(): return {'status':'ok'}
@app.post('/v1/analyze')
def analyze(req:AnalyzeRequest):
 try:return agent.analyze(req.question)
 except ValueError as e:raise HTTPException(400,str(e))
