import streamlit as st
import pandas as pd
import sqlite3
import plotly.express as px

# ---------------- PAGE SETTINGS ----------------

st.set_page_config(
    page_title="Financial Advisor",
    page_icon="💰",
    layout="wide"
)

st.title("💰 Financial Advisor & Expense Manager")
st.write("Track your expenses and get smart financial advice")

# ---------------- DATABASE ----------------

conn = sqlite3.connect("finance.db", check_same_thread=False)

cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS expenses(
id INTEGER PRIMARY KEY AUTOINCREMENT,
category TEXT,
amount REAL
)
""")

conn.commit()

# ---------------- LOAD DATA ----------------

def load_data():

    return pd.read_sql_query(
        "SELECT * FROM expenses",
        conn
    )

# ---------------- SIDEBAR ----------------

page = st.sidebar.selectbox(
    "Select Page",
    [
        "Dashboard",
        "Add Expense",
        "Expense History",
        "Analytics",
        "Budget Planner",
        "Savings Goal",
        "AI Budget Advice"
    ]
)

df = load_data()

# ---------------- DASHBOARD ----------------

if page == "Dashboard":

    st.header("📊 Dashboard")

    total = df["amount"].sum() if not df.empty else 0

    count = len(df)

    highest = "None"

    if not df.empty:

        highest = (
            df.groupby("category")["amount"]
            .sum()
            .idxmax()
        )

    c1,c2,c3 = st.columns(3)

    c1.metric("Total Expenses",f"₹{total}")

    c2.metric("Transactions",count)

    c3.metric("Highest Category",highest)

# ---------------- ADD EXPENSE ----------------

elif page=="Add Expense":

    st.header("➕ Add Expense")

    category = st.selectbox(
        "Category",
        [
            "Food",
            "Transport",
            "Shopping",
            "Entertainment",
            "Bills",
            "Other"
        ]
    )

    amount = st.number_input(
        "Amount",
        min_value=0.0
    )

    if st.button("Add Expense",key="add"):

        cursor.execute(
            """
            INSERT INTO expenses(category,amount)
            VALUES(?,?)
            """,
            (category,amount)
        )

        conn.commit()

        st.success("Expense Added Successfully")

# ---------------- HISTORY ----------------

elif page=="Expense History":

    st.header("📋 Expense History")

    df = load_data()

    st.dataframe(df)

    st.subheader("Delete Expense")

    if not df.empty:

        expense_id = st.selectbox(
            "Expense ID",
            df["id"]
        )

        if st.button("Delete",key="delete"):

            cursor.execute(
                "DELETE FROM expenses WHERE id=?",
                (int(expense_id),)
            )

            conn.commit()

            st.success("Expense Deleted")

# ---------------- ANALYTICS ----------------

elif page=="Analytics":

    st.header("📈 Analytics")

    if not df.empty:

        fig1 = px.pie(
            df,
            names="category",
            values="amount",
            title="Expense Distribution"
        )

        st.plotly_chart(fig1)

        bar_df = (
            df.groupby("category")["amount"]
            .sum()
            .reset_index()
        )

        fig2 = px.bar(
            bar_df,
            x="category",
            y="amount",
            title="Category Wise Expenses"
        )

        st.plotly_chart(fig2)

    else:

        st.warning("No expenses available")

# ---------------- BUDGET ----------------

elif page=="Budget Planner":

    st.header("🎯 Budget Planner")

    income = st.number_input(
        "Monthly Income",
        min_value=0.0
    )

    budget = st.number_input(
        "Budget Limit",
        min_value=0.0
    )

    total = df["amount"].sum() if not df.empty else 0

    st.write("Current Expenses : ₹",total)

    if total > budget:

        st.error("⚠ Budget Exceeded")

    else:

        st.success("✔ Within Budget")

        st.write(
            "Remaining Budget : ₹",
            budget-total
        )

# ---------------- SAVINGS ----------------

elif page=="Savings Goal":

    st.header("🏦 Savings Goal Tracker")

    goal = st.number_input(
        "Target Savings",
        min_value=1.0
    )

    saved = st.number_input(
        "Current Savings",
        min_value=0.0
    )

    progress = saved/goal

    st.progress(min(progress,1.0))

    st.write(
        f"{progress*100:.1f}% Completed"
    )

# ---------------- AI BUDGET ADVICE ----------------

elif page == "AI Budget Advice":

    st.header("🤖 AI Financial Advisor")

    salary = st.number_input(
        "Enter Monthly Salary (₹)",
        min_value=0.0
    )

    spent = st.number_input(
        "Enter Amount Spent This Month (₹)",
        min_value=0.0
    )

    savings = st.number_input(
        "Current Savings (₹)",
        min_value=0.0
    )

    if st.button("Get AI Advice"):

        remaining = salary - spent

        st.subheader("📊 Financial Summary")

        st.write("Monthly Salary :", f"₹{salary}")

        st.write("Amount Spent :", f"₹{spent}")

        st.write("Money Left :", f"₹{remaining}")

        st.write("Current Savings :", f"₹{savings}")

        # 50/30/20 Rule

        needs = salary * 0.50

        wants = salary * 0.30

        invest = salary * 0.20

        st.subheader("📚 Recommended Budget (50/30/20 Rule)")

        st.write(f"Needs : ₹{needs:.0f}")

        st.write(f"Wants : ₹{wants:.0f}")

        st.write(f"Savings : ₹{invest:.0f}")

        # Expense advice

        if spent > salary:

            st.error(
                "⚠ You are spending more than your salary."
            )

            st.write(
                "Reduce unnecessary expenses immediately."
            )

        elif spent > salary * 0.8:

            st.warning(
                "You are spending more than 80% of your income."
            )

            st.write(
                "Try increasing your savings rate."
            )

        else:

            st.success(
                "Excellent! Your expenses are under control."
            )

        # Savings goal

        goal = salary * 6

        st.subheader("🏦 Recommended Emergency Fund")

        st.write(
            f"Suggested Savings Goal: ₹{goal:.0f}"
        )

        if savings >= goal:

            st.success(
                "You have achieved your emergency fund target!"
            )

        else:

            remaining_goal = goal - savings

            st.info(
                f"You need ₹{remaining_goal:.0f} more to reach your goal."
            )

        # Additional advice

        st.subheader("💡 AI Suggestions")

        st.write("✔ Save at least 20% of income every month.")

        st.write("✔ Avoid impulse shopping.")

        st.write("✔ Keep 3-6 months of expenses as emergency fund.")

        st.write("✔ Invest regularly through SIP or Mutual Funds.")

        st.write("✔ Track every expense.")

# ---------------- DOWNLOAD CSV ----------------

st.sidebar.subheader("Download Data")

csv = load_data().to_csv(index=False)

st.sidebar.download_button(
    "Download CSV",
    csv,
    "expenses.csv",
    "text/csv"
)

conn.close()