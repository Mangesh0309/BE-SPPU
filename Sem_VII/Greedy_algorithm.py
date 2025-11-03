# Job Sequencing with Deadlines using Greedy Algorithm

# A job class to store job details
class Job:
    def __init__(self, job_id, deadline, profit):
        self.job_id = job_id
        self.deadline = deadline
        self.profit = profit

# Function to perform job sequencing
def job_sequencing(jobs):
    # Step 1: Sort jobs by profit in descending order
    jobs.sort(key=lambda x: x.profit, reverse=True)

    n=len(jobs)
    result = [False] * n # To track free time slots
    job_order = ['-1'] * n # To store job sequence results 

    # Step 2: Schedule each job in its last possible slot before the deadline
    for job in jobs: 
        # Check for last available slot before deadline
        for j in range(min(n, job.deadline) - 1, -1, -1):
            if not result[j]: # If slot is free
                result[j] = True
                job_order[j] = job.job_id
                break
    
    # Step 3: Display the final Scheduled jobs
    print("Scheduled Jobs: ", [job for job in job_order if job != '-1'])

    # Calculate total profit
    total_profit = sum(job.profit for job in jobs if job.job_id in job_order)
    print("Total Profit: ", total_profit)
    
# Driver code 
if __name__ == "__main__":
    n = int(input("Enter number of jobs: "))
    jobs = []

    for i in range(n):
        job_id = input(f"Enter Job ID for job {i+1}: ")
        deadline = int(input(f"Enter Deadline for job {i+1}: "))
        profit = int(input(f"Enter Profit for job {i+1}: "))
        jobs.append(Job(job_id , deadline , profit))
        print() 

    job_sequencing(jobs)
    
