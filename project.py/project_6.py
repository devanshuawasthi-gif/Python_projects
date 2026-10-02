import csv
import os
import time
import random
from datetime import datetime

import streamlit as st
import pandas as pd


# ==========================================
# PAGE SETTINGS
# ==========================================

st.set_page_config(
    page_title="AMUL Milk Collection",
    page_icon="🥛",
    layout="centered"
)


# ==========================================
# CUSTOMER DATABASE
# ==========================================

customers = {
    "000069": "AJAY KUMAR AWAST",
    "000070": "RAHUL KUMAR",
    "000071": "AMIT SINGH",
    "000072": "ROHIT KUMAR",
    "000073": "VIKAS YADAV"
}


# ==========================================
# CSV FILE
# ==========================================

csv_file = "milk_records.csv"

if not os.path.exists(csv_file):

    with open(csv_file, "w", newline="") as file:

        writer = csv.writer(file)

        writer.writerow([
            "Date",
            "Time",
            "Customer Code",
            "Customer Name",
            "Weight (kg)",
            "FAT",
            "SNF",
            "Water (%)",
            "Rate",
            "Amount"
        ])


# ==========================================
# MILK ANALYZER
# ==========================================

def milk_machine():

    # --------------------------------------
    # SIMULATED MACHINE READINGS
    # --------------------------------------

    # Weight of milk
    weight = round(random.uniform(1.0, 20.0), 2)

    # Milk quality readings
    fat = round(random.uniform(5.0, 8.5), 2)

    snf = round(random.uniform(8.5, 10.0), 2)

    # Water detected in milk
    water = round(random.uniform(0.0, 5.0), 2)

    return weight, fat, snf, water


# ==========================================
# RATE CALCULATION
# ==========================================

def calculate_rate(fat, snf):

    # Example formula.
    # Replace this with your actual dairy
    # FAT/SNF rate chart.

    rate = (fat * 5.00) + (snf * 2.00) + 9.46

    return rate


# ==========================================
# HEADER
# ==========================================

st.title("🥛 AMUL MILK COLLECTION")

st.markdown("---")


# ==========================================
# CUSTOMER
# ==========================================

st.subheader("👤 Customer Details")

customer_code = st.text_input(
    "Enter Customer Code",
    max_chars=6
)

customer_name = ""


if customer_code:

    if customer_code in customers:

        customer_name = customers[customer_code]

        st.success(
            f"Customer Found: {customer_name}"
        )

    else:

        st.error("Customer Code Not Found!")


# ==========================================
# START ANALYZER
# ==========================================

st.subheader("🔬 Milk Analyzer")


if st.button("▶ Start Milk Analyzer"):

    if customer_code not in customers:

        st.error("Please enter a valid Customer Code.")

    else:

        # ----------------------------------
        # PROCESSING
        # ----------------------------------

        with st.spinner(
            "Milk analyzer processing..."
        ):

            time.sleep(1)

            weight, fat, snf, water = milk_machine()

        st.success("✅ Milk Analysis Complete!")


        # ----------------------------------
        # DISPLAY MACHINE VALUES
        # ----------------------------------

        st.subheader("📊 Automatic Machine Reading")


        col1, col2 = st.columns(2)

        with col1:

            st.metric(
                "Milk Weight",
                f"{weight:.2f} kg"
            )

        with col2:

            st.metric(
                "Water",
                f"{water:.2f} %"
            )


        col3, col4 = st.columns(2)

        with col3:

            st.metric(
                "FAT",
                f"{fat:.2f}"
            )

        with col4:

            st.metric(
                "SNF",
                f"{snf:.2f}"
            )


        # ==================================
        # WATER STATUS
        # ==================================

        if water == 0:

            st.success(
                "✅ No added water detected"
            )

        elif water <= 2:

            st.warning(
                f"⚠ Small amount of water detected: {water:.2f}%"
            )

        else:

            st.error(
                f"⚠ High water detected: {water:.2f}%"
            )


        # ==================================
        # RATE
        # ==================================

        rate = calculate_rate(
            fat,
            snf
        )


        # ==================================
        # AMOUNT
        # ==================================

        amount = weight * rate


        st.markdown("---")

        st.subheader("💰 Payment Calculation")


        col1, col2, col3 = st.columns(3)

        with col1:

            st.metric(
                "Weight",
                f"{weight:.2f} kg"
            )

        with col2:

            st.metric(
                "Rate",
                f"₹{rate:.2f}/kg"
            )

        with col3:

            st.metric(
                "Amount",
                f"₹{amount:.2f}"
            )


        # ==================================
        # DATE AND TIME
        # ==================================

        now = datetime.now()

        date = now.strftime(
            "%d-%m-%Y"
        )

        current_time = now.strftime(
            "%H:%M:%S"
        )


        # ==================================
        # SAVE CSV
        # ==================================

        with open(
            csv_file,
            "a",
            newline=""
        ) as file:

            writer = csv.writer(file)

            writer.writerow([

                date,

                current_time,

                customer_code,

                customer_name,

                f"{weight:.2f}",

                f"{fat:.2f}",

                f"{snf:.2f}",

                f"{water:.2f}",

                f"{rate:.2f}",

                f"{amount:.2f}"

            ])


        st.success(
            "✅ Transaction saved successfully!"
        )


        # ==================================
        # RECEIPT
        # ==================================

        st.markdown("---")

        st.subheader(
            "🧾 Milk Purchase Slip"
        )


        slip = f"""
        <div style="
            width:390px;
            margin:auto;
            padding:15px;
            background:white;
            color:black;
            font-family:monospace;
            font-size:13px;
            border:1px solid black;
        ">

        <div style="
            text-align:center;
            font-weight:bold;
            font-size:18px;
        ">
            KASOLAR (5245)
        </div>

        <div style="
            text-align:center;
            font-weight:bold;
            font-size:15px;
        ">
            MILK PURCHASE
        </div>

        <hr style="
            border-top:1px dashed black;
        ">

        <table style="width:100%;">

        <tr>
        <td>Date</td>
        <td>{date}</td>
        </tr>

        <tr>
        <td>Record No</td>
        <td>7728</td>
        </tr>

        <tr>
        <td>Code</td>
        <td>{customer_code}</td>
        </tr>

        <tr>
        <td>Name</td>
        <td>{customer_name}</td>
        </tr>

        </table>

        <hr style="
            border-top:1px dashed black;
        ">

        <table style="
            width:100%;
            text-align:center;
        ">

        <tr>

        <th>Weight</th>
        <th>FAT</th>
        <th>SNF</th>
        <th>Water</th>

        </tr>

        <tr>

        <td>{weight:.2f} kg</td>
        <td>{fat:.2f}</td>
        <td>{snf:.2f}</td>
        <td>{water:.2f}%</td>

        </tr>

        </table>

        <hr style="
            border-top:1px dashed black;
        ">

        <table style="width:100%;">

        <tr>
        <td>Rate</td>
        <td style="text-align:right;">
        ₹{rate:.2f}/kg
        </td>
        </tr>

        <tr>
        <td><b>Amount</b></td>
        <td style="
            text-align:right;
            font-weight:bold;
        ">
        ₹{amount:.2f}
        </td>
        </tr>

        </table>

        <hr style="
            border-top:1px dashed black;
        ">

        <div style="text-align:center;">
        Print Time: {date} {current_time}
        </div>

        <br>

        <div style="
            text-align:center;
            font-weight:bold;
        ">
        AMUL AMCS
        </div>

        </div>
        """


        st.markdown(
            slip,
            unsafe_allow_html=True
        )


# ==========================================
# PREVIOUS RECORDS
# ==========================================

st.markdown("---")

st.subheader("📋 Previous Milk Records")


if os.path.exists(csv_file):

    df = pd.read_csv(csv_file)

    if not df.empty:

        st.dataframe(
            df,
            use_container_width=True
        )

    else:

        st.info(
            "No records available."
        )