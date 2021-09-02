def solution(table, languages, preference):
    job_score = {}
    for job in table:
        job = job.split(' ')
        JOB = job[0]
        
        table = {job[1]:5, job[2]:4, job[3]:3, job[4]:2, job[5]:1}    # dict for table score
        engineer = dict(zip(languages, preference))                   # dict for engineer preference
        
        languages_both = set(table.keys()) & set(engineer.keys())     # get languages for both(table & engineer)
                                                                      # to lower time cost(if not, test failed)
        score = 0
        for language in languages_both:
            score += table[language]*engineer[language]               # multiple score & preference
        job_score[JOB] = score                                        # get total score for each job
    
    # get first max scored job
    maxJOB = [job for job in job_score.keys() if job_score[job]==max(job_score.values())]   
    maxJOB.sort()                                                     

    answer = maxJOB[0]
    return answer