import streamlit as st
from currentaccount import currentAccount

if 'account' not in st.session_state:
    st.session_state.account = currentAccount(balance=10000 )
st.set_page_config(page_title="Current Account", layout="centered")
st.title("Current Account")

balance_placeholder = st.empty()
balance_placeholder.subheader(f"Balance: N{st.session_state.account.balance}")
with st.form("current_account_form"):
    amount = st.number_input("Enter amount", min_value=1000, step=100)
    operations = st.selectbox("Deposit or withdraw", ("Deposit", "Withdraw"))
    submit = st.form_submit_button("Submit")

    if submit:
        try:
            if operations == "Deposit":
                st.session_state.account.deposit(amount)
                st.success(f"Successfuly Depositted N{amount}")
            # add elif statement here for withdraw function
            elif operations == "Withdraw":
                st.session_state.account.withdraw(amount)
                st.success(f"Successfully Withdrew N{amount}!")
            balance_placeholder.subheader(f"Balance: N{st.session_state.account.balance}")
        except ValueError as e:
            st.error(str(e))