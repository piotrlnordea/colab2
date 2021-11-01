# -*- coding: utf-8 -*-
"""
Created on Wed Sep 15 09:56:37 2021

@author: M017824
"""

# -*- coding: utf-8 -*-
"""
Created on Mon Sep 13 21:35:58 2021
@author: user
"""

from transformers import pipeline
from transformers import AutoTokenizer, AutoModelForQuestionAnswering
import torch
import matplotlib.pyplot as plt
modelname = 'bert-large-uncased-whole-word-masking-finetuned-squad'
tokenizer = AutoTokenizer.from_pretrained(modelname)
model = AutoModelForQuestionAnswering.from_pretrained(modelname)

model.base_model.config

text = r"""The objective is to be compliant to Nordea test strategy and to provide a clear description of test scope, planned test activities and test approaches. Additionally, all required agreements, prerequisites and dependencies for this test object are stated in this plan.  
Primary stakeholders (e.g. product owner or other business representative) for the test object are:  
In chapter 3.2.1 Test documentation structure, the relationship between other test planning and reporting documents are presented. 
PB ACT - Advisory Cockpit Tool is a Nordic advisory tool that helps  PB advisers in on boarding new clients into Private Banking. ACT is used by PB advisor for daily activities.
Details of the technical solution are to be found in the High-Level Design (HLD) / Solution Architecture (SAD) documents and in the Solution Design document, please see link in chapter.
Currently, the volume of users is very less as we are still in roll out phase of application to end users. hence the performance tests are out of scope. Structured Performance tests using tool like Load Runner are not performed in PB ACT.
Test processes and test activities directly cater to the development lifecycle and quality of final delivery. It acts as a horizontal and is an in-step which during many phases of development cycle. Scrum team includes a test analyst who is responsible for the test activities within the team. This helps in giving an insight into the overall future delivery. Product backlog is defined by Product Owner (henceforth referred as PO) of scrum team. Test case designing, manual execution and defect management will be managed by tool JIRA.
Design authority team is mainly responsible to provide approval on design level changes proposed by team to accommodate the new feature.
Discovery team  comprises of Project manager/Technical Architect /Solution Architect/PO responsible for finalizing high level business requirement, Technical solutions to implement the business requirement
Before writing Test scenario or Test cases, Tester will do the analysis of story and clarify his doubts with PO and BA. Once test scenarios are prepared, Tester along with Developer will have walkthrough with BA/PO to confirm the test scenarios. Similarly when execution is over again Tester will have the walkthrough of Test results with PO, hence here PO gets the opportunity to find the gap or defect that are not caught in Test life cycle. 
"""

import numpy as np
def get_top_answers(possible_starts,possible_ends,input_ids):
  answers = []
  for start,end in zip(possible_starts,possible_ends):
    
    answer = tokenizer.convert_tokens_to_string(tokenizer.convert_ids_to_tokens(input_ids[start:end+1]))
    answers.append( answer )
  return answers  

def answer_question(question,context,topN):

    inputs = tokenizer.encode_plus(question, context, add_special_tokens=True, return_tensors="pt")
    
    input_ids = inputs["input_ids"].tolist()[0]

    text_tokens = tokenizer.convert_ids_to_tokens(input_ids)
    model_out = model(**inputs)
     
    answer_start_scores = model_out["start_logits"]
    answer_end_scores = model_out["end_logits"]

    possible_starts = np.argsort(answer_start_scores.cpu().detach().numpy()).flatten()[::-1][:topN]
    possible_ends = np.argsort(answer_end_scores.cpu().detach().numpy()).flatten()[::-1][:topN]
    
    #get best answer
    answer_start = torch.argmax(answer_start_scores)  
    answer_end = torch.argmax(answer_end_scores) + 1  # Get the most likely end of answer with the argmax of the score

    answer = tokenizer.convert_tokens_to_string(tokenizer.convert_ids_to_tokens(input_ids[answer_start:answer_end]))

    answers = get_top_answers(possible_starts,possible_ends,input_ids )

    return { "answer":answer,"answer_start":answer_start,"answer_end":answer_end,"input_ids":input_ids,
            "answer_start_scores":answer_start_scores,"answer_end_scores":answer_end_scores,"inputs":inputs,"answers":answers,
            "possible_starts":possible_starts,"possible_ends":possible_ends}

questions = [
    " What is the purpose of compliance assesment ? ",
    "Is the defect management process agreed with all key stakeholders participating in defect management ?",
    "Are all tools listed in the master test plan ?",
    "Are any of the Nordea standard defect management tools used ?",
    "What are we talking about?",
    "What is the main idea here?",
    "Do you have all mandatory QA execution metrics implemented ?",
    "Are all tools listed in the master test plan ? ",
    " Is the test process implemented considering test automation ? ",
    "What is the IT area for the IT iniative ?" ,
    " What is the name for the IT Initiative ?" ,
    "Is the written English language understandable ?",
    " What are the resiliency level of applications in your cluster? ",
    "Is any release test plan created based on the Nordea test strategy 4.0 release test plan template?"
]


i=0;
for q in questions:
  answer_map = answer_question(q,text,5)   
  i+=1
  print( "\n", i, ".Question:",q)
 
  print("Answers:")
  [print((index+1)," ) ",ans) for index,ans in  enumerate(answer_map["answers"]) if len(ans) > 0 ]
  
#answer_map = answer_question("Where is most populous in the world?",text,3)