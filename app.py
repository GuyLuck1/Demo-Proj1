import streamlit as st
# משימה 1
st.title("📚 מערכת ציונים בבית הספר")

st.subheader("ברוכים הבאים למערכת הציונים!")

# קלט שם
name = st.text_input("מה השם שלך?")

if name:
    st.write("שלום", name, "!")

# קלט גיל
age = st.number_input("בן/בת כמה אתה?", min_value=0, max_value=120, step=1)

if age < 18:
    st.write("נשארו לך", 18 - age, "שנים עד גיל 18.")
else:
    st.write("כבר הגעת לגיל 18!")

# כפתור
if st.button("לחץ כאן"):
    st.success("הכפתור נלחץ בהצלחה!")


# משימה 2 - ציונים
st.subheader("📝 בדיקת הציון שלך")

grade = st.number_input(
    "מה הציון שלך?",
    min_value=0,
    max_value=100,
    step=1
)

# הודעת סטטוס לפי הציון
if grade >= 90:
    st.success("כל הכבוד " + name + "! קיבלת ציון מצוין: " + str(grade))

elif grade >= 60:
    st.info(name + ", קיבלת ציון " + str(grade) + " ועברת את המבחן.")

else:
    st.warning(name + ", קיבלת ציון " + str(grade) + ". כדאי ללמוד יותר למבחן הבא.")


# כפתור בדיקת ציון
if st.button("בדוק את הציון"):
    st.success(name + ", הציון שלך הוא " + str(grade))


# מחשבון חיבור ציונים
st.subheader("🧮 מחשבון חיבור ציונים")

grade1 = st.number_input(
    "הכנס ציון ראשון",
    min_value=0,
    max_value=100,
    step=1
)

grade2 = st.number_input(
    "הכנס ציון שני",
    min_value=0,
    max_value=100,
    step=1
)

if st.button("חשב סכום"):
    total = grade1 + grade2
    st.write("סכום שני הציונים הוא:", total)
