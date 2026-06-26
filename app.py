import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
# data loading
users=pd.read_excel("data/EduPro.xlsx",sheet_name="Users")
courses=pd.read_excel("data/EduPro.xlsx",sheet_name="Courses")
transactions=pd.read_excel("data/EduPro.xlsx",sheet_name="Transactions")
# data processing
users['AgeGroup']=pd.cut(
    users["Age"],
    bins=(14,17,25,35),
    labels=["15-17","18-25","26-35"]
)
user_transactions=pd.merge(transactions,users, on="UserID")
   

user_course_data=pd.merge(user_transactions,courses,on="CourseID")

# page configuration
st.set_page_config(
    page_title="EduPro Learning Analytics Dashbord",
    layout="wide")

# dashboard title


st.title("EduPro Learning Analytics Dashboard")
st.markdown("Data-Driven Insights into Learner Behaviour and Course Engagement")

# sidebar
st.sidebar.title("EduPro Analytics")
st.sidebar.success("Education Analyst Project")

# dataset overview cards
col1,col2,col3=st.columns(3)

# KPI creation.......

st.markdown("### Key Performance Indicators")
# col1,col2,col3,col4,col5 = st.columns(5)
# with col1:
#    total_enrollments=len(user_course_data)
#    st.metric("Total Enrollments",total_enrollments)
# with col2:
#     st.metric("Most Active Age Group","26-35")
# with col3:
#     st.metric("Female Perticipation","50.78%")
# with col4:
#     st.metric("Top Category","Data Science")
# with col5:
#     st.metric("Preferred Level","Beginner")
st.markdown("""
<style>
.card{
        padding:15px;
        border_radius:10px;
        text-align:center;
        color:white}
.value{
    font-size:28px;
    font-weight:bold}
.label{font-size:14px}
</style>
""",unsafe_allow_html=True)
total_enrollments=len(user_course_data)
col1,col2,col3,col4,col5 = st.columns(5)
with col1:
    st.markdown(f"""
    <div class="card" style="background-color:#1f77b4;">
        <div class="value">{total_enrollments}</div>
        <div class="label">Total Enrollments</div>
    </div>
    """,unsafe_allow_html=True)
with col2:
    st.markdown(f"""
    <div class="card" style="background-color:#2ca02c;">
        <div class="value">26-35</div>
        <div class="label">Most Active Age Group</div>
    </div>
    """,unsafe_allow_html=True)
with col3:
    st.markdown(f"""
    <div class="card" style="background-color:#9467bd;">
        <div class="value">50.78%</div>
        <div class="label">Female Participation</div>
    </div>
    """,unsafe_allow_html=True)
with col4:
    st.markdown(f"""
    <div class="card" style="background-color:#ff7f0e;">
        <div class="value">Data Science</div>
        <div class="label">Top Category</div>
    </div>
    """,unsafe_allow_html=True)
with col5:
    st.markdown(f"""
    <div class="card" style="background-color:#d62728;">
        <div class="value">Beginner</div>
        <div class="label">Preferred Level</div>
    </div>
    """,unsafe_allow_html=True)



# Chart creation.....

st.markdown("----------")
col1,col2 =st.columns(2, gap="medium")
with col1:
    st.subheader("Age Group Activity")
    age_activity=user_transactions["AgeGroup"].value_counts()
    fig1,ax1=plt.subplots(figsize=(6,4))
    age_activity.plot(
    kind="bar",
    color="teal",
    ax=ax1
)
    for i,v in enumerate(age_activity):
       ax1.text(i,v+50, str(v), ha="center")
    ax1.set_xlabel('Age Group')
    ax1.set_ylabel("Enrollments")
    st.pyplot(fig1)
with col2:
    st.subheader("Gender Participation Ratio")
    fig2, ax2 = plt.subplots(figsize=(6,4))
    ax2.pie(
        [5078,4922],
        labels=["Female","Male"],
        autopct='%1.1f%%',
        startangle=90,
        colors=["teal","gold"]
    )
    st.pyplot(fig2)
st.markdown("------")
st.subheader("Course Category vs Enrollments")
category_enrollment=pd.Series({
    "Data Science":916,
    "Finance":864,
    "Web Development":844,
    "Business":833,
    "project Management":829,
    "Artificial Intelligence":829,
    "Design":827,
    "Cyber Security":819,
    "Machine Learning":819,
    "Digital Marketing":808,
    "Marketing":806,
    "Programming":806
})
fig3,ax3=plt.subplots(figsize=(10,5))
category_enrollment.plot(kind="bar",color="teal",ax=ax3)
for i,v in enumerate(category_enrollment):
    ax3.text(i,v+5,str(v), ha="center",fontsize=8)
ax3.set_title("Course Category Popularity")
ax3.set_xlabel("Course Category")
ax3.set_ylabel("Enrollments")
plt.xticks(rotation=45)
st.pyplot(fig3)

st.markdown('----')
st.subheader("Course Category vs Gender Distribution")
gender_based_difference=pd.crosstab(
    user_course_data["Gender"],
    user_course_data["CourseCategory"]
)
fig4,ax4=plt.subplots(figsize=(12,6))
gender_based_difference.T.plot(kind="bar",ax=ax4)
for container in ax4.containers:
    ax4.bar_label(container,fmt="%d",padding =2)
ax4.set_title("Course Category vs Gender Distribution")
ax4.set_xlabel("Course Category")
ax4.set_ylabel("Enrollments")
ax4.legend(title="Gender")
plt.xticks(rotation=45)
plt.tight_layout()
st.pyplot(fig4)

st.markdown('-----')
col1,col2=st.columns(2)
with col1:
   st.subheader("Course Level Preference Distribution")
   course_level_counts=pd.Series({
    "Beginner":3573,
    "Advanced":3475,
    "Intermediate":2952
})
fig5,ax5=plt.subplots(figsize=(6,4))
course_level_counts.plot(kind="bar",color="green",ax=ax5)
for i,v in enumerate(course_level_counts):
    ax5.text(i,v+20,str(v), ha="center")
ax5.set_xlabel("Course Level")
ax5.set_ylabel("Number of Learners")
plt.xticks(rotation=0)
plt.tight_layout()
st.pyplot(fig5)
with col2:
    st.subheader("Course Type vs Course Level")
    course_type_level =pd.DataFrame({
        "Free":[2005,2395,2003],
        "Paid":[1470,1178,949]

    },index=["Advanced","Beginner","Intermediate"])
fig6,ax6=plt.subplots(figsize=(8,5))
course_type_level.plot(
    kind="bar",
    stacked=True,
    ax=ax6
)
for container in ax6.containers:
    ax6.bar_label(container,fmt="%d")
    ax6.text(i,v+20,str(v), ha="center")
ax6.set_xlabel("Course Level")
ax6.set_ylabel("Enrollments")
ax6.legend(title="Course Type")
plt.xticks(rotation=0)
plt.tight_layout()
st.pyplot(fig6)

#footer
st.divider()
st.caption(
    "EduPro Analytics Dashboard | Built using Python,Pandas, Matplotlib and Streamlit"
)
