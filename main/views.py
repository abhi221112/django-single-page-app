# views.py
from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    html_content = """
    <!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Abhishek Maurya – CV</title>
    <style>
        :root {
            --primary-color: #2c3e50;
            --secondary-color: #3498db;
            --accent-color: #e74c3c;
            --light-color: #ecf0f1;
            --dark-color: #2c3e50;
            --text-color: #333;
            --light-text: #777;
            --shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        }
        
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }
        
        body {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            line-height: 1.6;
            color: var(--text-color);
            background: linear-gradient(135deg, #f5f7fa 0%, #c3cfe2 100%);
            padding: 20px;
            min-height: 100vh;
        }
        
        .container {
            max-width: 1000px;
            margin: 0 auto;
            background: white;
            box-shadow: var(--shadow);
            border-radius: 10px;
            overflow: hidden;
        }
        
        header {
            background: linear-gradient(135deg, var(--primary-color), var(--secondary-color));
            color: white;
            padding: 2rem;
            text-align: center;
        }
        
        h1 {
            font-size: 2.5rem;
            margin-bottom: 0.5rem;
        }
        
        .title {
            font-size: 1.2rem;
            margin-bottom: 1rem;
            font-weight: 400;
        }
        
        .contact-info {
            display: flex;
            justify-content: center;
            gap: 2rem;
            margin-top: 1rem;
            flex-wrap: wrap;
        }
        
        .contact-item {
            display: flex;
            align-items: center;
            gap: 0.5rem;
            background: rgba(255, 255, 255, 0.2);
            padding: 0.5rem 1rem;
            border-radius: 50px;
        }
        
        main {
            padding: 2rem;
        }
        
        .section {
            margin-bottom: 2.5rem;
        }
        
        h2 {
            color: var(--primary-color);
            padding-bottom: 0.5rem;
            margin-bottom: 1rem;
            border-bottom: 2px solid var(--secondary-color);
            display: inline-block;
        }
        
        h3 {
            color: var(--secondary-color);
            margin-bottom: 0.5rem;
        }
        
        h4 {
            color: var(--primary-color);
            margin: 1rem 0 0.5rem 0;
        }
        
        .subheading {
            color: var(--light-text);
            font-style: italic;
            margin-bottom: 1rem;
        }
        
        ul {
            list-style-type: none;
            padding-left: 0;
        }
        
        li {
            margin-bottom: 0.8rem;
            padding-left: 1.5rem;
            position: relative;
        }
        
        li:before {
            content: "•";
            color: var(--secondary-color);
            font-weight: bold;
            position: absolute;
            left: 0;
        }
        
        .skills-grid {
            display: grid;
            grid-template-columns: repeat(auto-fill, minmax(300px, 1fr));
            gap: 1.5rem;
            margin-top: 1rem;
        }
        
        .skill-category {
            background: var(--light-color);
            padding: 1rem;
            border-radius: 5px;
            box-shadow: var(--shadow);
        }
        
        .skill-category h4 {
            margin-bottom: 0.5rem;
            color: var(--primary-color);
        }
        
        .skill-items {
            display: flex;
            flex-wrap: wrap;
            gap: 0.5rem;
        }
        
        .skill-item {
            background: white;
            padding: 0.3rem 0.8rem;
            border-radius: 20px;
            font-size: 0.9rem;
            border: 1px solid var(--secondary-color);
        }
        
        .experience-item, .internship-item {
            margin-bottom: 1.5rem;
            padding: 1rem;
            border-left: 3px solid var(--secondary-color);
            background: var(--light-color);
            border-radius: 0 5px 5px 0;
        }
        
        .print-btn {
            position: fixed;
            bottom: 2rem;
            right: 2rem;
            background: var(--secondary-color);
            color: white;
            border: none;
            padding: 0.8rem 1.5rem;
            border-radius: 50px;
            cursor: pointer;
            box-shadow: var(--shadow);
            transition: all 0.3s ease;
            font-size: 1rem;
            z-index: 100;
        }
        
        .print-btn:hover {
            background: var(--primary-color);
            transform: translateY(-3px);
        }
        
        .project-highlight {
            background: white;
            padding: 1rem;
            border-radius: 5px;
            margin: 1rem 0;
            box-shadow: var(--shadow);
        }
        
        .tag {
            display: inline-block;
            background: var(--secondary-color);
            color: white;
            padding: 0.2rem 0.6rem;
            border-radius: 4px;
            font-size: 0.8rem;
            margin-right: 0.5rem;
        }
        
        @media (max-width: 768px) {
            .contact-info {
                flex-direction: column;
                gap: 0.5rem;
                align-items: center;
            }
            
            .skills-grid {
                grid-template-columns: 1fr;
            }
            
            h1 {
                font-size: 2rem;
            }
            
            main {
                padding: 1.5rem;
            }
            
            header {
                padding: 1.5rem;
            }
        }
        
        @media print {
            .print-btn {
                display: none;
            }
            
            body {
                background: white;
                padding: 0;
            }
            
            .container {
                box-shadow: none;
                border-radius: 0;
            }
        }
        
        .footer {
            text-align: center;
            padding: 1rem;
            background: var(--primary-color);
            color: white;
        }
    </style>
</head>
<body>
    <div class="container">
        <header>
            <h1>Abhishek Maurya</h1>
            <div class="title">Software Engineer</div>
            <div class="contact-info">
                <div class="contact-item">
                    <span>📞</span>
                    <span>9936721146</span>
                </div>
                <div class="contact-item">
                    <span>📧</span>
                    <span>abhishekkmaurya654@gmail.com</span>
                </div>
            </div>
        </header>
        
        <main>
            <section class="section">
                <h2>Professional Summary</h2>
                <p>Python developer with 3 years of hands-on experience in developing scalable web applications using Flask, Django, and FastAPI. Proficient in cloud technologies such as AWS and Azure, with a passion for designing optimized and maintainable code.</p>
            </section>
            
            <section class="section">
                <h2>Skills</h2>
                <div class="skills-grid">
                    <div class="skill-category">
                        <h4>Languages/Frameworks</h4>
                        <div class="skill-items">
                            <span class="skill-item">Python</span>
                            <span class="skill-item">Django</span>
                            <span class="skill-item">Flask</span>
                            <span class="skill-item">FastAPI</span>
                        </div>
                    </div>
                    
                    <div class="skill-category">
                        <h4>APIs</h4>
                        <div class="skill-items">
                            <span class="skill-item">Flask API</span>
                            <span class="skill-item">Django Rest Framework</span>
                            <span class="skill-item">Flask-JWT-Extended</span>
                        </div>
                    </div>
                    
                    <div class="skill-category">
                        <h4>Databases</h4>
                        <div class="skill-items">
                            <span class="skill-item">PostgreSQL</span>
                            <span class="skill-item">SQLAlchemy</span>
                            <span class="skill-item">Flask-SQLAlchemy</span>
                        </div>
                    </div>
                    
                    <div class="skill-category">
                        <h4>Authentication</h4>
                        <div class="skill-items">
                            <span class="skill-item">Django Allauth</span>
                        </div>
                    </div>
                    
                    <div class="skill-category">
                        <h4>Tools & Libraries</h4>
                        <div class="skill-items">
                            <span class="skill-item">Postman</span>
                            <span class="skill-item">Selenium</span>
                            <span class="skill-item">Power BI</span>
                            <span class="skill-item">pytest</span>
                            <span class="skill-item">requests</span>
                            <span class="skill-item">Pandas</span>
                            <span class="skill-item">Numpy</span>
                            <span class="skill-item">OpenCV</span>
                        </div>
                    </div>
                    
                    <div class="skill-category">
                        <h4>Cloud/DevOps</h4>
                        <div class="skill-items">
                            <span class="skill-item">AWS</span>
                            <span class="skill-item">Microsoft Azure</span>
                            <span class="skill-item">DevOps</span>
                        </div>
                    </div>
                    
                    <div class="skill-category">
                        <h4>Other</h4>
                        <div class="skill-items">
                            <span class="skill-item">Competitive Analysis</span>
                        </div>
                    </div>
                </div>
            </section>
            
            <section class="section">
                <h2>Experience</h2>
                <div class="experience-item">
                    <h3>Python Developer</h3>
                    <div class="subheading">RMSI Private Limited | 06/2022 – Present</div>
                    <ul>
                        <li>Built and deployed RESTful APIs using Flask, Django Rest Framework, and FastAPI.</li>
                    </ul>
                    
                    <h4>Key Projects:</h4>
                    
                    <div class="project-highlight">
                        <div class="tag">Flask</div>
                        <div class="tag">REST API</div>
                        <div class="tag">Supply Chain</div>
                        <h4>Dabur QR Code Tracker</h4>
                        <p>Developed RESTful APIs for a mobile app that tracks honey supply chain stages—from beekeepers to vendors—using Flask REST framework.</p>
                    </div>
                    
                    <div class="project-highlight">
                        <div class="tag">Python</div>
                        <div class="tag">Flask/Django</div>
                        <div class="tag">PostgreSQL</div>
                        <h4>Mahendra Tech – Project Management Tool</h4>
                        <p>Built a collaborative project management system for task assignment, progress tracking, and report generation using Python (Flask/Django) and PostgreSQL. Focused on collaboration tools, data visualization, and REST APIs.</p>
                    </div>
                    
                    <div class="project-highlight">
                        <div class="tag">Django/Flask</div>
                        <div class="tag">React.js/Angular</div>
                        <div class="tag">PostgreSQL/MySQL</div>
                        <h4>Tata AIG – Insurance Claim Management System</h4>
                        <p>Developed a digital platform enabling customers to file and track insurance claims online, improving transparency and reducing processing time. Utilized Python (Django/Flask) for backend, integrated frontend technologies (React.js/Angular), and managed databases (PostgreSQL/MySQL).</p>
                    </div>
                    
                    <ul>
                        <li>E-commerce API: Developed a scalable RESTful API for handling authentication, payments, and order management.</li>
                        <li>Real-time Chat Application: Built a live chat system with WebSocket integration and JWT authentication.</li>
                        <li>Weather Data Scraper: Automated weather data extraction with AWS Lambda and S3.</li>
                        <li>ML Model Deployment: Deployed a churn prediction model using FastAPI, Docker, and AWS ECS.</li>
                        <li>Dashboards: Created multiple dashboards using Power BI for data visualization and insights.</li>
                    </ul>
                </div>
            </section>
            
            <section class="section">
                <h2>Education</h2>
                <h3>B.Tech - Computer Science & Engineering</h3>
                <div class="subheading">Technocrats Institute of Technology Excellence | 02/2018 - 06/2022</div>
                <p>Score: 85%</p>
            </section>
            
            <section class="section">
                <h2>Internships</h2>
                
                <div class="internship-item">
                    <h3>Python Developer Intern</h3>
                    <div class="subheading">Codervalue Solutions Private Limited | 03/2022 - 05/2022</div>
                    <ul>
                        <li>Extracted customer reviews via web scraping, improving product ranking by 87%.</li>
                        <li>Developed APIs using Flask for seamless web integration.</li>
                    </ul>
                </div>
                
                <div class="internship-item">
                    <h3>Intern Trainee</h3>
                    <div class="subheading">Air India | 06/2021 - 08/2021</div>
                    <ul>
                        <li>Worked in Network and Cyber Security focusing on operations and maintenance.</li>
                    </ul>
                </div>
                
                <div class="internship-item">
                    <h3>Python Trainee</h3>
                    <div class="subheading">Corecard | 02/2020 - 05/2020</div>
                    <ul>
                        <li>Built a predictive model for Uber ride demand analysis, optimizing pricing and route efficiency.</li>
                    </ul>
                </div>
            </section>
        </main>
        
        <div class="footer">
            <p>Abhishek Maurya - Updated 2025</p>
        </div>
    </div>
    
    <button class="print-btn" onclick="window.print()">Print CV</button>
    
    <script>
        // Simple animation for page elements
        document.addEventListener('DOMContentLoaded', function() {
            const sections = document.querySelectorAll('.section');
            sections.forEach((section, index) => {
                section.style.opacity = '0';
                section.style.transform = 'translateY(20px)';
                section.style.transition = 'opacity 0.5s ease, transform 0.5s ease';
                
                setTimeout(() => {
                    section.style.opacity = '1';
                    section.style.transform = 'translateY(0)';
                }, 100 + (index * 100));
            });
            
            // Add subtle animation to project highlights on hover
            const projects = document.querySelectorAll('.project-highlight');
            projects.forEach(project => {
                project.addEventListener('mouseenter', () => {
                    project.style.transform = 'translateY(-5px)';
                    project.style.transition = 'transform 0.3s ease';
                });
                
                project.addEventListener('mouseleave', () => {
                    project.style.transform = 'translateY(0)';
                });
            });
        });
    </script>
</body>
</html>
    """
    return HttpResponse(html_content)