# =====================================================
# CampusAI - Green Turtle Arts and Science College
# Final Enhanced Version - BCA Final Year Project
# =====================================================

COLLEGE_NAME = "Green Turtle Arts and Science College"
COLLEGE_ADDRESS = "No. 45, Green Valley Road, vellore - 600028, Tamil Nadu"
COLLEGE_PHONE = "+91 98765 43210"
COLLEGE_EMAIL = "info@greenturtle.edu.in"
PRINCIPAL = "Dr. Green Turtle"

# Departments and HODs
DEPARTMENTS = {
    "Computer Science": {"HOD": "Dr. Red- eared silder", "email": "red-ear.slider@greenturtle.edu.in"},
    "Mathematics": {"HOD": "Prof. painted turtle", "email": "painted.Turtle@greenturtle.edu.in"},
    "Physics": {"HOD": "Dr. Box Turtle", "email": "box.turtle@greenturtle.edu.in"},
    "Chemistry": {"HOD": "Dr. Snapping Turtle", "email": "snapping.turtle@greenturtle.edu.in"},
    "English": {"HOD": "Prof. Diamondback Terrapin", "email": "diamondback.terrapin@greenturtle.edu.in"},
    "Commerce": {"HOD": "Dr. Softshell Turtle", "email": "softshell.turtle@greenturtle.edu.in"},
    "Psychology": {"HOD": "Prof. Green sea Turtle", "email": "greensea.turtle@greenturtle.edu.in"}
}

# Courses with Shift
COURSES = {
    "BCA": {"dept": "Computer Science", "duration": "3 Years", "fees": 45000, "shift": "Evening"},
    "B.Sc Computer Science": {"dept": "Computer Science", "duration": "3 Years", "fees": 48000, "shift": "Evening"},
    "B.Sc Artificial Intelligence & Data Science": {"dept": "Computer Science", "duration": "3 Years", "fees": 55000, "shift": "Evening"},
    "B.Sc Mathematics": {"dept": "Mathematics", "duration": "3 Years", "fees": 40000, "shift": "Morning"},
    "B.Sc Physics": {"dept": "Physics", "duration": "3 Years", "fees": 42000, "shift": "Morning"},
    "B.Sc Chemistry": {"dept": "Chemistry", "duration": "3 Years", "fees": 43000, "shift": "Morning"},
    "B.A English Literature": {"dept": "English", "duration": "3 Years", "fees": 35000, "shift": "Morning"},
    "B.Com General": {"dept": "Commerce", "duration": "3 Years", "fees": 38000, "shift": "Evening"},
    "B.Com Corporate Secretaryship": {"dept": "Commerce", "duration": "3 Years", "fees": 40000, "shift": "Evening"},
    "B.Sc Psychology": {"dept": "Psychology", "duration": "3 Years", "fees": 41000, "shift": "Evening"}
}

# Full Syllabus
SYLLABUS = {
    "BCA": "C Programming, Data Structures, DBMS, Operating Systems, Java, Python, Web Development, Software Engineering, Cloud Computing, Computer Networks, Project Work.",
    "B.Sc Computer Science": "Digital Electronics, Programming in C++, Data Structures, Algorithms, Database Management, Computer Networks, Operating Systems, AI Basics, Machine Learning Fundamentals.",
    "B.Sc Artificial Intelligence & Data Science": "Python for Data Science, Machine Learning, Deep Learning, Data Visualization, Big Data Analytics, NLP, Statistics.",
    "B.Sc Mathematics": "Algebra, Calculus, Differential Equations, Real Analysis, Complex Analysis, Statistics, Numerical Methods.",
    "B.Sc Physics": "Classical Mechanics, Thermodynamics, Electromagnetism, Quantum Mechanics, Optics, Solid State Physics, Nuclear Physics.",
    "B.Sc Chemistry": "Inorganic, Organic, Physical Chemistry, Analytical Chemistry, Biochemistry, Environmental Chemistry.",
    "B.A English Literature": "Shakespeare, Romantic Poetry, Victorian Literature, Indian Writing, Literary Criticism, Modern Fiction.",
    "B.Com General": "Accounting, Business Management, Economics, Marketing, Taxation, Auditing.",
    "B.Com Corporate Secretaryship": "Company Law, Secretarial Practice, Corporate Governance, Business Law.",
    "B.Sc Psychology": "General Psychology, Developmental Psychology, Abnormal Psychology, Social Psychology, Counselling Psychology."
}

# ===================== UPDATED TIMETABLE =====================

TIMETABLE = {
    "BCA": """**BCA (Evening Shift - 12:30 PM to 5:00 PM)**

Monday:
1. Python Programming (Lab)
2. Data Structures
3. DBMS
4. Break
5. Operating Systems
6. Web Development Lab

Tuesday:
1. Java Programming
2. Software Engineering
3. Computer Networks
4. Break
5. Cloud Computing
6. Cyber Security Elective

Wednesday:
1. Python Lab
2. DBMS Lab
3. Aptitude Training
4. Break
5. Mini Project
6. Seminar

Thursday:
1. Java Lab
2. Data Structures
3. Operating Systems
4. Break
5. Web Technologies
6. Project Guidance

Friday:
1. Cloud Computing
2. Networks
3. Soft Skills
4. Break
5. Practical Revision
6. Viva Preparation""",

    "B.Sc Computer Science": """**B.Sc Computer Science (Evening Shift)**

Monday:
1. Digital Electronics
2. C++ Programming
3. Data Structures
4. Break
5. Algorithms
6. Lab

Tuesday:
1. DBMS
2. Operating Systems
3. Networks
4. Break
5. AI Basics
6. Lab

Wednesday:
1. Theory Class
2. Software Engineering
3. Project Work
4. Break
5. Aptitude
6. Seminar

Thursday:
1. Java
2. Python
3. Algorithms Practice
4. Break
5. Lab
6. Case Study

Friday:
1. Revision
2. Mock Test
3. Viva
4. Break
5. Lab Exam
6. Project Review""",

    "B.Sc Artificial Intelligence & Data Science": """**B.Sc AIDS (Evening Shift)**

Monday:
1. Python for DS
2. Statistics
3. Machine Learning
4. Break
5. Data Visualization
6. Lab

Tuesday:
1. Deep Learning
2. Big Data Analytics
3. NLP
4. Break
5. Project Work
6. Lab

Wednesday:
1. R Programming
2. Data Mining
3. AI Theory
4. Break
5. Seminar
6. Lab

Thursday:
1. ML Lab
2. Power BI
3. Data Cleaning
4. Break
5. Project Guidance
6. Workshop

Friday:
1. AI Applications
2. Cloud AI
3. Soft Skills
4. Break
5. Revision
6. Viva""",

    "B.Sc Mathematics": """**B.Sc Mathematics (Morning Shift)**

Monday:
1. Algebra
2. Calculus
3. Differential Equations
4. Break
5. Real Analysis
6. Tutorial

Tuesday:
1. Discrete Math
2. Statistics
3. Numerical Methods
4. Break
5. Complex Analysis
6. Problem Solving

Wednesday:
1. Linear Algebra
2. Probability
3. Equations
4. Break
5. Assignment
6. Seminar

Thursday:
1. Vector Calculus
2. Optimization
3. Lab Work
4. Break
5. Practice
6. Doubt Session

Friday:
1. Revision
2. Model Test
3. Viva
4. Break
5. Worksheet
6. Exam Prep""",

    "B.Sc Physics": """**B.Sc Physics (Morning Shift)**

Monday:
1. Classical Mechanics
2. Thermodynamics
3. Electromagnetism
4. Break
5. Optics
6. Lab

Tuesday:
1. Quantum Mechanics
2. Nuclear Physics
3. Solid State
4. Break
5. Electronics
6. Lab

Wednesday:
1. Mathematical Physics
2. Waves
3. Lab
4. Break
5. Seminar
6. Assignment

Thursday:
1. Computational Physics
2. Instrumentation
3. Practical
4. Break
5. Viva
6. Lab

Friday:
1. Revision
2. Mock Test
3. Problems
4. Break
5. Lab Prep
6. Viva""",

    "B.Sc Chemistry": """**B.Sc Chemistry (Morning Shift)**

Monday:
1. Inorganic
2. Organic
3. Physical
4. Break
5. Analytical
6. Lab

Tuesday:
1. Biochemistry
2. Environmental
3. Lab
4. Break
5. Seminar
6. Theory

Wednesday:
1. Reaction Mechanism
2. Spectroscopy
3. Physical Lab
4. Break
5. Assignment
6. Viva

Thursday:
1. Chemical Bonding
2. Industrial Chem
3. Lab
4. Break
5. Project
6. Revision

Friday:
1. Revision
2. Model Test
3. Practical Prep
4. Break
5. Record Work
6. Viva""",

    "B.A English Literature": """**B.A English Literature (Morning Shift)**

Monday:
1. Shakespeare
2. Romantic Poetry
3. Criticism
4. Break
5. Indian Writing
6. Drama

Tuesday:
1. Victorian Literature
2. Modern Fiction
3. Creative Writing
4. Break
5. Linguistics
6. Seminar

Wednesday:
1. American Literature
2. Postcolonial
3. Essay Writing
4. Break
5. Assignment
6. Tutorial

Thursday:
1. Literary Theory
2. Drama Analysis
3. Reading
4. Break
5. Presentation
6. Discussion

Friday:
1. Revision
2. Mock Test
3. Viva
4. Break
5. Writing
6. Seminar""",

    "B.Com General": """**B.Com General (Evening Shift)**

Monday:
1. Accounting
2. Management
3. Economics
4. Break
5. Marketing
6. Taxation

Tuesday:
1. Corporate Law
2. Auditing
3. Banking
4. Break
5. GST
6. Case Study

Wednesday:
1. Cost Accounting
2. Statistics
3. Income Tax
4. Break
5. Assignment
6. Seminar

Thursday:
1. Finance
2. E-Commerce
3. Practical
4. Break
5. Project
6. Revision

Friday:
1. Revision
2. Mock Test
3. Viva
4. Break
5. Prep
6. Workshop""",

    "B.Com Corporate Secretaryship": """**B.Com Corporate Secretaryship (Evening Shift)**

Monday:
1. Company Law
2. Secretarial Practice
3. Governance
4. Break
5. Communication
6. Law

Tuesday:
1. Accounting
2. Finance
3. Case Study
4. Break
5. Practice
6. Seminar

Wednesday:
1. Corporate Law
2. Taxation
3. Documentation
4. Break
5. Assignment
6. Viva

Thursday:
1. Office Management
2. Law Practice
3. Project
4. Break
5. Revision
6. Workshop

Friday:
1. Revision
2. Model Test
3. Presentation
4. Break
5. Prep
6. Viva""",

    "B.Sc Psychology": """**B.Sc Psychology (Evening Shift)**

Monday:
1. General Psychology
2. Developmental
3. Abnormal Psychology
4. Break
5. Social Psychology
6. Research Methods

Tuesday:
1. Counselling
2. Behavior Science
3. Case Study
4. Break
5. Practical
6. Seminar

Wednesday:
1. Cognitive Psychology
2. Personality
3. Lab
4. Break
5. Assignment
6. Discussion

Thursday:
1. Clinical Psychology
2. Mental Health
3. Observation
4. Break
5. Report Writing
6. Viva

Friday:
1. Revision
2. Mock Test
3. Field Work
4. Break
5. Prep
6. Seminar"""
}

# ===================== UPDATED FACULTY =====================

FACULTY = {
    "BCA": [
    {"name": "Prof. Leatherback Turtle", "subject": "Python Programming & Lab"},
    {"name": "Dr. Olive Ridley", "subject": "DBMS & Data Structures"},
    {"name": "Mr. Softshell Turtle", "subject": "Operating Systems & Networks"},
    {"name": "Ms. Hawksbill Turtle", "subject": "Web Development"},
    {"name": "Mr. Diamondback Terrapin", "subject": "Java Programming"}
],

"B.Sc Computer Science": [
    {"name": "Prof. Loggerhead Turtle", "subject": "C++ Programming"},
    {"name": "Ms. Painted Turtle", "subject": "Computer Networks"},
    {"name": "Dr. Snapping Turtle", "subject": "Algorithms"},
    {"name": "Mr. Musk Turtle", "subject": "Operating Systems"},
    {"name": "Ms. Green Sea Turtle", "subject": "AI Basics"}
],

"B.Sc Artificial Intelligence & Data Science": [
    {"name": "Dr. Box Turtle", "subject": "Machine Learning"},
    {"name": "Ms. Sea Turtle", "subject": "Data Science"},
    {"name": "Mr. Red-Eared Slider", "subject": "Big Data"},
    {"name": "Dr. Map Turtle", "subject": "Deep Learning"},
    {"name": "Ms. Spotted Turtle", "subject": "NLP & AI Tools"}
],

"B.Sc Mathematics": [
    {"name": "Prof. Mud Turtle", "subject": "Calculus"},
    {"name": "Mr. Wood Turtle", "subject": "Statistics"},
    {"name": "Dr. Pond Turtle", "subject": "Real Analysis"},
    {"name": "Ms. River Turtle", "subject": "Numerical Methods"}
],

"B.Sc Physics": [
    {"name": "Dr. Flatback Turtle", "subject": "Quantum Mechanics"},
    {"name": "Prof. Black Marsh Turtle", "subject": "Electromagnetism"},
    {"name": "Mr. Caspian Turtle", "subject": "Thermodynamics"},
    {"name": "Dr. Mata Mata", "subject": "Optics & Labs"}
],

"B.Sc Chemistry": [
    {"name": "Dr. Chinese Softshell", "subject": "Organic Chemistry"},
    {"name": "Mr. Fly River Turtle", "subject": "Physical Chemistry"},
    {"name": "Dr. African Helmeted Turtle", "subject": "Biochemistry"},
    {"name": "Ms. Golden Thread Turtle", "subject": "Analytical Chemistry"}
],

"B.A English Literature": [
    {"name": "Prof. Asian Leaf Turtle", "subject": "Shakespeare"},
    {"name": "Ms. Indian Star Turtle", "subject": "Poetry & Criticism"},
    {"name": "Dr. Sulcata Tortoise", "subject": "Literary Theory"},
    {"name": "Mr. Greek Tortoise", "subject": "Modern Literature"}
],

"B.Com General": [
    {"name": "Dr. Leopard Tortoise", "subject": "Accounting"},
    {"name": "Ms. Radiated Tortoise", "subject": "Management"},
    {"name": "Mr. Aldabra Tortoise", "subject": "Economics"},
    {"name": "Ms. Desert Tortoise", "subject": "Auditing"}
],

"B.Com Corporate Secretaryship": [
    {"name": "Dr. Hermann Tortoise", "subject": "Company Law"},
    {"name": "Mr. Gopher Tortoise", "subject": "Corporate Governance"},
    {"name": "Ms. Pancake Tortoise", "subject": "Secretarial Practice"},
    {"name": "Mr. Elongated Tortoise", "subject": "Business Law"}
],

"B.Sc Psychology": [
    {"name": "Prof. Egyptian Tortoise", "subject": "Abnormal Psychology"},
    {"name": "Ms. Marginated Tortoise", "subject": "Counselling Psychology"},
    {"name": "Dr. Russian Tortoise", "subject": "Clinical Psychology"},
    {"name": "Ms. Galápagos Tortoise", "subject": "Social Psychology"}
]
}

def get_response(user_input):
    if not user_input or not user_input.strip():
        return "Hello! 👋 Welcome to Green Turtle CampusAI. How can I assist you today?"

    text = user_input.lower().strip()

    # ====================== GREETINGS ======================
    if any(word in text for word in ["hi", "hello", "hey", "namaste", "good morning", "good afternoon"]):
        return f"Hello! 👋 Welcome to **{COLLEGE_NAME}**.\nHow can I help you today?"

    # ====================== THANK YOU ======================
    elif any(word in text for word in ["thank", "thanks", "thank you"]):
        return "You're most welcome! 😊 Feel free to ask anything else."

    # ====================== COLLEGE INFO ======================
    elif any(word in text for word in ["college", "about", "principal", "address", "contact", "phone", "email"]):
        return f"""**{COLLEGE_NAME}**
📍 {COLLEGE_ADDRESS}
📞 {COLLEGE_PHONE}
✉️ {COLLEGE_EMAIL}
👨‍🏫 Principal: {PRINCIPAL}"""

    # ====================== COURSES ======================
    elif any(word in text for word in ["course", "courses", "offered", "available", "list"]):
        course_list = "\n".join([f"• {course}" for course in COURSES.keys()])
        return f"**Courses Offered at Green Turtle**\n\n{course_list}\n\nReply with course name for details (e.g., 'BCA syllabus' or 'BCA fees')."

    # ====================== FEES ======================
    elif any(word in text for word in ["fee", "fees", "cost", "amount", "tuition", "price"]):
        fees_text = "\n".join([f"• {c}: ₹{info['fees']:,}" for c, info in COURSES.items()])
        return f"**Annual Fees (2026-27)**\n\n{fees_text}\n\n*Note: Fees are subject to change. Contact admission office.*"

    # ====================== SYLLABUS ======================
    elif "syllabus" in text:
        for course in SYLLABUS:
            if course.lower() in text or course.replace(" ", "").lower() in text:
                return f"**{course} Syllabus**\n{SYLLABUS[course]}"
        return "Please specify the course. Example: 'BCA syllabus' or 'Physics syllabus'"

    # ====================== TIMETABLE ======================
    elif any(word in text for word in ["timetable", "time table", "schedule", "class timing", "timetable"]):
        for key in TIMETABLE:
            if key.lower() in text:
                return f"**Timetable - {key}**\n{TIMETABLE[key]}"
        return "Please specify your course and year.\nExample: 'BCA 3rd year timetable'"

    # ====================== HOD ======================
    elif "hod" in text or "head of department" in text or "head" in text:
        for dept in DEPARTMENTS:
            if dept.lower() in text:
                info = DEPARTMENTS[dept]
                return f"**HOD - {dept}**\n👨‍🏫 {info['HOD']}\n✉️ {info['email']}"
        return "Please mention the department name.\nExample: 'HOD Computer Science'"

    # ====================== FACULTY ======================
    elif any(word in text for word in ["faculty", "teacher", "staff", "professor", "lecturer"]):
        for course in FACULTY:
            if course.lower() in text:
                fac_list = "\n".join([f"• {f['name']} - {f['subject']}" for f in FACULTY[course]])
                return f"**Faculty Members - {course}**\n{fac_list}"
        return "Please mention the course.\nExample: 'BCA faculty' or 'Physics faculty'"

    # ====================== EXAMS ======================
    elif any(word in text for word in ["exam", "exams", "semester", "hall ticket", "result"]):
        return """**Examination Details**

• End Semester Exams start from **15th November 2026**
• Hall Tickets will be issued 7 days before exams
• Internal assessments are ongoing"""

    # ====================== ADMISSION ======================
    elif any(word in text for word in ["admission", "admit", "apply", "enroll", "join", "eligibility"]):
        return """**Admissions 2026-27**

• Admissions are currently open
• Required Documents: 10th & 12th Marksheets, ID Proof, Photos
• Contact Admission Cell: +91 98765 43210"""

    # ====================== COLLEGE TIMINGS ======================
    elif any(word in text for word in ["timing", "time", "shift", "open", "close", "class time"]):
        return """**College Timings**

🕘 Morning Shift : 8:00 AM – 1:30 PM
🕒 Evening Shift : 12:30 PM – 5:00 PM

Note: Practical & Lab classes may extend beyond regular hours."""

    # ====================== DEFAULT RESPONSE ======================
    else:
        return """I'm sorry, I couldn't understand your question. 😊

**You can ask me about:**
• Courses & Syllabus
• Fees Structure
• Timetable
• HOD / Faculty
• Exams & Hall Ticket
• Admissions
• College Information

Try examples:
- "BCA syllabus"
- "HOD Computer Science"
- "College fees"
- "BCA 3rd year timetable"
"""

# ====================== TESTING ======================
if __name__ == "__main__":
    print(f"✅ {COLLEGE_NAME} CampusAI is Ready!")
    print("Type 'exit' or 'quit' to stop.\n")
    
    while True:
        user_input = input("You: ")
        if user_input.lower() in ["exit", "quit", "bye"]:
            print("Bot: Goodbye! All the best for your studies! 👋")
            break
        response = get_response(user_input)
        print("Bot:", response)
        print("-" * 60)