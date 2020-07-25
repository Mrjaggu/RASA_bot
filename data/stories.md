

## happy path               <!-- name of the story - just for debugging -->
* greet              
  - utter_greet


## think path  
* think
  - utter_think

## think path2  
* greet
  - utter_greet
* think
  - utter_think
  - utter_did_that_help
* affirm or thanks
  - utter_gratitude

## think path3  
* think
  - utter_think
  - utter_did_that_help
* affirm or thanks
  - utter_gratitude  
* deny
  - utter_ask_again
* think
  - utter_think
  - utter_did_that_help
* affirm or thanks
  - utter_gratitude
* goodbye
  - utter_goodbye

## think path4
* greet
  - utter_greet
* think
  - utter_think
  - utter_did_that_help
* affirm or thanks
  - utter_gratitude
  - utter_more
* goodbye
  - utter_goodbye


## think path5
* think
  - utter_think
  - utter_did_that_help
* deny
  - utter_ask_again
* think
  - utter_think
  - utter_did_that_help
* affirm or thanks
  - utter_gratitude
* goodbye
  - utter_goodbye


## think path6
* greet
  - utter_greet
* think
  - utter_think
  - utter_did_that_help
* deny
  - utter_ask_again
* think
  - utter_think
  - utter_did_that_help
* affirm or thanks
  - utter_gratitude
* goodbye
  - utter_goodbye

## think path7
* think
  - utter_think
  - utter_did_that_help
* affirm or thanks
  - utter_gratitude

## think path8
* greet
  - utter_greet
* think
  - utter_think
  - utter_did_that_help
* affirm or thanks
  - utter_gratitude
  - utter_more
* thanks
  - utter_gratitude
* goodbye
  - utter_goodbye


## job criteria path
* greet
  - utter_greet
* skills_job{"CRITERIA": "criteria"}
  - slot{"CRITERIA": "criteria"}    
  - action_criteria
  - utter_did_that_help
* affirm or thanks
  - utter_gratitude
* goodbye
  - utter_goodbye

## job criteria path2
* greet
  - utter_greet
* skills_job{"CRITERIA": "possibility","COMPANY":'Google'}
  - slot{"CRITERIA": "criteria","COMPANY":"Google"}    
  - action_criteria
  - utter_did_that_help
* affirm or thanks
  - utter_gratitude
  - utter_more
* thanks
  - utter_gratitude
* goodbye
  - utter_goodbye  



## job profile path
* greet
  - utter_greet
* job_profile
  - action_openning
  - utter_did_that_help
* affirm or thanks
  - utter_gratitude
* goodbye
  - utter_goodbye


## company address path
* greet
  - utter_greet
* company_address
  - action_address
  - utter_did_that_help
* affirm or thanks
  - utter_gratitude
* goodbye
  - utter_goodbye


## interview round path
* greet
  - utter_greet
* interview_round
  - action_interview_round
  - utter_did_that_help
* affirm or thanks
  - utter_gratitude
* goodbye
  - utter_goodbye


## application path
* greet
  - utter_greet
* application_status
  - action_application
  - utter_did_that_help
* affirm or thanks
  - utter_gratitude
* goodbye
  - utter_goodbye


## interview document path
* greet
  - utter_greet
* interview_document
  - action_document
  - utter_did_that_help
* affirm or thanks
  - utter_gratitude
* goodbye
  - utter_goodbye

## stupid question path
* greet
  - utter_greet
* stupid
  - utter_stupid_question
  - utter_did_that_help
* affirm or thanks
  - utter_gratitude
* goodbye
  - utter_goodbye  


## holidays
* greet
  - utter_greet
* holidays
  - utter_holidays
  - utter_did_that_help
* affirm or thanks
  - utter_gratitude
* goodbye
  - utter_goodbye


## user ideal path
* greet
  - utter_greet
* user_ideal
  - utter_user_ideal
  - utter_did_that_help
* affirm or thanks
  - utter_gratitude
* goodbye
  - utter_goodbye


## helpful path
* greet
  - utter_greet
* helpful
  - utter_helpful
  - utter_did_that_help
* affirm or thanks
  - utter_gratitude
* goodbye
  - utter_goodbye


## company instructions path
* greet
  - utter_greet
* company_instructions
  - action_instruction
  - utter_did_that_help
* affirm or thanks
  - utter_gratitude
* goodbye
  - utter_goodbye


## popular company path
* greet
  - utter_greet
* popular_company
  - action_popular
  - utter_did_that_help
* affirm or thanks
  - utter_gratitude
* goodbye
  - utter_goodbye  

## company job time path
* greet
  - utter_greet
* company_job_time
  - action_timing
  - utter_did_that_help
* affirm or thanks
  - utter_gratitude
* goodbye
  - utter_goodbye


## company apti ans path
* greet
  - utter_greet
* company_apti_ans
  - action_apti_answer
  - utter_did_that_help
* affirm or thanks
  - utter_gratitude
* goodbye
  - utter_goodbye


## company better path
* greet
  - utter_greet
* company_better
  - action_compare
  - utter_did_that_help
* affirm or thanks
  - utter_gratitude
* goodbye
  - utter_goodbye


## company achievement path
* greet
  - utter_greet
* company_achievement
  - action_achievement
  - utter_did_that_help
* affirm or thanks
  - utter_gratitude
* goodbye
  - utter_goodbye


## interview time path
* greet
  - utter_greet
* interview_time
  - action_interview_time
  - utter_did_that_help
* affirm or thanks
  - utter_gratitude
* goodbye
  - utter_goodbye

## salary path
* greet
  - utter_greet
* salary
  - utter_salary
  - utter_did_that_help
* affirm or thanks
  - utter_gratitude
* goodbye
  - utter_goodbye

## interview taker path
* greet
  - utter_greet
* charge
  - action_incharge
  - utter_did_that_help
* affirm or thanks
  - utter_gratitude
* goodbye
  - utter_goodbye  

## company vacancies path
* greet
  - utter_greet
* company_vacancies
  - action_vacancy
  - utter_did_that_help
* affirm or thanks
  - utter_gratitude
* goodbye
  - utter_goodbye

## job match path
* greet
  - utter_greet
* job_match
  - utter_job_match
  - utter_did_that_help
* affirm or thanks
  - utter_gratitude
* goodbye
  - utter_goodbye


## work LMN employee
* greet
  - utter_greet
* LMN
  - action_lmn
  - utter_did_that_help
* affirm or thanks
  - utter_gratitude
* goodbye
  - utter_goodbye

## interview success path
* greet
  - utter_greet
* interview_success
  - utter_interview_success
  - utter_did_that_help
* affirm or thanks
  - utter_gratitude
* goodbye
  - utter_goodbye


## company motto
* greet
  - utter_greet
* company_motto
  - action_motto
  - utter_did_that_help
* affirm or thanks
  - utter_gratitude
* goodbye
  - utter_goodbye


## interview date path
* greet
  - utter_greet
* interview_date
  - utter_interview_date
  - utter_did_that_help
* affirm or thanks
  - utter_gratitude
* goodbye
  - utter_goodbye

## interview history path  
* greet
  - utter_greet
* interview_history
  - action_interview_history
  - utter_did_that_help
* affirm or thanks
  - utter_gratitude
* goodbye
  - utter_goodbye


## job description applied path
* greet
  - utter_greet
* job_description_applied
  - action_job_description_applied
  - utter_did_that_help
* affirm or thanks
  - utter_gratitude
* goodbye
  - utter_goodbye

## eligibility path
* greet
  - utter_greet
* eligibility_criteria
  - action_eligibility_criteria
  - utter_did_that_help
* affirm or thanks
  - utter_gratitude
* goodbye
  - utter_goodbye

## hate path
* hate
  - utter_hate
  - utter_did_that_help
* affirm or thanks
  - utter_gratitude
* goodbye
  - utter_goodbye  

## say goodbye
* goodbye
  - utter_goodbye

## fallback
- utter_unclear


