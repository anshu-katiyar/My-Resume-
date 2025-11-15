import streamlit as st
import streamlit.components.v1 as components

# Page config
st.set_page_config(
    page_title="Anshu Katiyar Resume",
    page_icon="📄",
    layout="wide"
)

# HTML content
html_content = """
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Anshu Katiyar Resume</title>

<link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap" rel="stylesheet">

<style>
    body {
        font-family: 'Inter', sans-serif;
        margin: 0;
        padding: 40px;
        background: #ffffff;
        color: #222;
    }

    .container {
        max-width: 1050px;
        margin: auto;
    }

    h1 {
        font-size: 34px;
        font-weight: 700;
        margin-bottom: 4px;
    }

    .sub-title {
        font-size: 18px;
        color: #4d4d4d;
    }

    .tagline {
        font-size: 14px;
        color: #777;
        margin-top: 4px;
    }

    .contact-box {
        display: grid;
        grid-template-columns: repeat(4, 1fr);
        border-top: 2px solid #dcdcdc;
        border-bottom: 2px solid #dcdcdc;
        padding: 12px 0;
        margin: 25px 0;
        font-size: 14px;
        color: #4d4d4d;
    }

    .contact-item {
        display: flex;
        gap: 8px;
        align-items: center;
    }

    .contact-item a {
        color: #4d4d4d;
        text-decoration: none;
        display: flex;
        gap: 8px;
        align-items: center;
    }

    .contact-item a:hover {
        color: #222;
        text-decoration: underline;
    }

    .grid {
        display: grid;
        grid-template-columns: 55% 45%;
        gap: 30px;
    }

    h2 {
        font-size: 18px;
        font-weight: 700;
        margin-top: 30px;
    }

    .bold {
        font-weight: 700;
    }

    .section-text {
        font-size: 14px;
        margin-top: 4px;
        line-height: 1.5;
    }

    ul {
        margin-top: 6px;
        padding-left: 20px;
        font-size: 14px;
    }

    .skill-box {
        display: flex;
        flex-wrap: wrap;
        gap: 8px;
        margin-top: 10px;
    }

    .skill {
        background: #dce2e8;
        padding: 4px 12px;
        border-radius: 6px;
        font-size: 13px;
        font-weight: 500;
    }

    @media print {
        body { padding: 0; }
    }
</style>
</head>

<body>
<div class="container">

    <h1>Anshu Katiyar</h1>
    <div class="sub-title">B.Tech in Computer Science & Engineering, 2027</div>
    <div class="tagline">Tradition , Prestige, Discipline</div>

    <div class="contact-box">

    <div class="contact-item">
        <a href="mailto:katiyaranshu00@gmail.com">
            <img src="https://img.icons8.com/ios-filled/20/000000/new-post.png" 
                 width="18" style="vertical-align:middle; margin-right:6px;">
            katiyaranshu00@gmail.com
        </a>
    </div>

    <div class="contact-item">
        <a href="tel:+919104274998">
            <img src="https://img.icons8.com/ios-filled/20/000000/phone.png" 
                 width="18" style="vertical-align:middle; margin-right:6px;">
            9104274998
        </a>
    </div>

    <div class="contact-item">
        <a href="https://maps.google.com/?q=Tutuichand,India" target="_blank">
            <img src="https://img.icons8.com/ios-filled/20/000000/marker.png" 
                 width="18" style="vertical-align:middle; margin-right:6px;">
            Kanpur, India
        </a>
    </div>

    <div class="contact-item">
        <span>
            <img src="https://img.icons8.com/ios-filled/20/000000/birthday.png" 
                 width="18" style="vertical-align:middle; margin-right:6px;">
            11, August 2006
        </span>
    </div>

    <div class="contact-item">
        <a href="https://linkedin.com/in/anshu-katiyar" target="_blank">
            <img src="https://blog.boon.so/wp-content/uploads/2024/03/LinkedIn-Logo-2-scaled.jpg" 
                 width="18" style="vertical-align:middle; margin-right:6px;">
            linkedin.com/in/anshu-katiyar
        </a>
    </div>

    <div class="contact-item">
        <a href="https://github.com/anshu-katiyar" target="_blank">
            <img src="https://github.githubassets.com/assets/GitHub-Mark-ea2971cee799.png" 
                 width="18" style="vertical-align:middle; margin-right:6px;">
            github.com/anshu-katiyar
        </a>
    </div>

</div>

    <div class="grid">
        <div>
            <h2>EDUCATION</h2>
            <div class="bold">B.Tech Computer science & Engineering</div>
            <div class="section-text">
                Ajay Kumar Garg Engineering College, Ghaziabad <br>
                09/2023 - 2027 &nbsp;&nbsp;&nbsp;&nbsp;     SGPA : <b>7.55</b>
            </div>

            <h2>RELEVANT COURSE</h2>
            <ul>
                <li>Python Programming</li>
                <li>Machine Learning</li>
                <li>Statistics & Probability</li>
                <li>Mathematics</li>
                <li>Linear Algebra</li>
                <li>Artificial Intelligence</li>
                <li>Data Structures & Algorithms</li>
            </ul>

            <h2>SKILLS</h2>
            <div class="skill-box">
                <div class="skill">Python</div>
                <div class="skill">Machine Learning</div>
                <div class="skill">Pandas & NumPy</div>
                <div class="skill">Matplotlib</div>
                <div class="skill">R Programming(basic)</div>
                <div class="skill">SQL</div>
                <div class="skill">Scikit-learn</div>
                <div class="skill">Git & Github</div>
                <div class="skill">Data visualization</div>
            </div>
            <h2>Tools</h2>
            <ul>
                <li>Excel</li>
                <li>Power BI</li>
                <li>Tableau</li>
                <li>jupyter Notebook</li>
            </ul>
            <h2>COMPETITIONS</h2>
            <div class="section-text bold">GEN AI EXCHANGE HACKATHON (2025)</div>
            <div class="section-text bold">E-cell IIT Bombay (2025)</div>

        </div>

        <div>
            <h2>PERSONAL PROJECTS</h2>
            <div class="bold">Real Time Traffic Prediction System<br>
            (08/2026 - 10/2025)</div>
            <ul>
                <li>URL : https://real-time-traffic-prediction-system-rshyh63h3zyrlw7zek9txc.streamlit.app/</li>
                <li>Predicts traffic congestion using Machine Learning</li>
                <li>Interactive dashboard with live maps</li>
                <li>Real time Analytics & weather impact analysis</li>
            </ul>

            <h2>CERTIFICATES</h2>

            <div class="bold">Data Analytics (07/2025 - 07/2025)</div>
            <div class="section-text">Data Analytics job Simulation certificate issued by FORAGE in complete virtual Internship</div>

            <div class="bold" style="margin-top:12px;">Tech-A-Thon 3.0 (10/2024 - 10/2024)</div>
            <div class="section-text">Organized by Birla Institute of Technology (BIT), Mesra, Ranchi</div>

            <div class="bold" style="margin-top:12px;">Quantum Computing (05/2025 - 05/2025)</div>
            <div class="section-text">Centre for Development of Advanced Computing, Hyderabad & IIT Roorkee with support of Government of India</div>

            <div class="bold" style="margin-top:12px;">Manthan (codeFest'24) (04/2024 - 04/2024)</div>
            <div class="section-text">Annual fest of Dept. of CSE, IIT (BHU) Varanasi</div>

            <h2>LANGUAGES</h2>
            <div class="section-text bold">Hindi</div>
            <div class="section-text">Native or Bilingual Proficiency</div>

            <div class="section-text bold" style="margin-top:8px;">English</div>
            <div class="section-text">Elementary Proficiency</div>

        </div>
    </div>

</div>
</body>
</html>
"""

# Display the HTML
components.html(html_content, height=1200, scrolling=True)