import streamlit as st

# Page setup
st.set_page_config(
    page_title="The Loan Wala | Modern Instant Lending",
    page_icon="⚡",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom High-End UI/UX CSS
st.markdown("""
<style>
    /* Dark Theme Base Styling */
    .stApp {
        background-color: #0F172A;
        color: #F8FAFC;
        font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;
    }
    
    /* Gradient Banner */
    .hero-container {
        background: linear-gradient(135deg, #1E1B4B 0%, #312E81 50%, #4338CA 100%);
        padding: 40px 30px;
        border-radius: 20px;
        text-align: center;
        border: 1px solid rgba(255, 255, 255, 0.1);
        box-shadow: 0 20px 25px -5px rgba(0, 0, 0, 0.5);
        margin-bottom: 30px;
    }
    .hero-title {
        font-size: 42px;
        font-weight: 900;
        letter-spacing: -1px;
        background: linear-gradient(180deg, #FFFFFF 0%, #A5B4FC 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin-bottom: 8px;
    }
    .hero-subtitle {
        color: #C7D2FE;
        font-size: 18px;
        font-weight: 400;
    }
    
    /* Custom Modern Cards */
    .metric-card {
        background: rgba(30, 41, 59, 0.7);
        backdrop-filter: blur(12px);
        border: 1px solid rgba(255, 255, 255, 0.08);
        padding: 24px;
        border-radius: 16px;
        text-align: center;
        box-shadow: 0 10px 15px -3px rgba(0, 0, 0, 0.3);
    }
    .metric-label {
        color: #94A3B8;
        font-size: 14px;
        font-weight: 500;
        text-transform: uppercase;
        letter-spacing: 0.5px;
    }
    .metric-value {
        color: #10B981;
        font-size: 32px;
        font-weight: 800;
        margin-top: 8px;
    }
    .metric-value-sub {
        color: #F3F4F6;
        font-size: 26px;
        font-weight: 700;
        margin-top: 8px;
    }
    
    /* Custom Button Style */
    .stButton>button {
        background: linear-gradient(135deg, #10B981 0%, #059669 100%);
        color: #FFFFFF;
        font-weight: 700;
        border-radius: 12px;
        border: none;
        padding: 12px 28px;
        width: 100%;
        transition: all 0.3s ease;
        box-shadow: 0 4px 14px 0 rgba(16, 185, 129, 0.39);
    }
    .stButton>button:hover {
        transform: translateY(-2px);
        box-shadow: 0 6px 20px 0 rgba(16, 185, 129, 0.55);
    }
    
    /* Feature Badge */
    .trust-badge {
        display: inline-block;
        background: rgba(16, 185, 129, 0.1);
        border: 1px solid rgba(16, 185, 129, 0.3);
        color: #34D399;
        padding: 6px 16px;
        border-radius: 9999px;
        font-size: 13px;
        font-weight: 600;
        margin-bottom: 12px;
    }
</style>
""", unsafe_allow_html=True)

# Top Hero Section
st.markdown("""
<div class="hero-container">
    <div class="trust-badge">🛡️ RBI Compliant NBFC Partners • 100% Paperless</div>
    <div class="hero-title">The Loan Wala ⚡</div>
    <div class="hero-subtitle">Get instant personal & business loans disbursed directly to your account in under 10 minutes.</div>
</div>
""", unsafe_allow_html=True)

# Navigation Layout
tab1, tab2, tab3 = st.tabs([
    "🧮 Smart EMI Calculator", 
    "🚀 Instant Eligibility & Onboarding", 
    "📊 Track Application Status"
])

# ----------------------------------------------------
# TAB 1: Smart Loan Calculator & Visualiser
# ----------------------------------------------------
with tab1:
    col_ctrl, col_res = st.columns([1.1, 0.9], gap="large")
    
    with col_ctrl:
        st.subheader("Customize Your Loan")
        
        amount = st.slider("Loan Amount Needed (₹)", min_value=5000, max_value=1000000, value=150000, step=5000)
        tenure = st.slider("Repayment Tenure (Months)", min_value=3, max_value=60, value=18, step=3)
        rate = st.slider("Interest Rate (% per annum)", min_value=9.0, max_value=36.0, value=13.5, step=0.5)
        
        r = (rate / 12) / 100
        emi = amount * r * ((1 + r)**tenure) / (((1 + r)**tenure) - 1) if r > 0 else amount / tenure
        total_pay = emi * tenure
        total_int = total_pay - amount

    with col_res:
        st.subheader("Payment Breakdown")
        
        # Display Glassmorphic Metric Cards
        st.markdown(f"""
        <div class="metric-card">
            <div class="metric-label">Estimated Monthly EMI</div>
            <div class="metric-value">₹{emi:,.0f}/mo</div>
        </div>
        """, unsafe_allow_html=True)
        
        st.write("")
        c1, c2 = st.columns(2)
        with c1:
            st.markdown(f"""
            <div class="metric-card">
                <div class="metric-label">Principal Amount</div>
                <div class="metric-value-sub">₹{amount:,.0f}</div>
            </div>
            """, unsafe_allow_html=True)
        with c2:
            st.markdown(f"""
            <div class="metric-card">
                <div class="metric-label">Total Interest</div>
                <div class="metric-value-sub" style="color: #F43F5E;">₹{total_int:,.0f}</div>
            </div>
            """, unsafe_allow_html=True)
            
        st.progress(amount / total_pay)
        st.caption(f"💡 **Principal:** {amount/total_pay*100:.1f}% | **Interest:** {total_int/total_pay*100:.1f}%")

# ----------------------------------------------------
# TAB 2: Instant Eligibility Flow (Interactive UI)
# ----------------------------------------------------
with tab2:
    st.subheader("Quick 3-Step Approval")
    
    # Progress Header
    step = st.radio("Step", ["1. Basic Info", "2. Income Verification", "3. Select Offer"], horizontal=True, label_visibility="collapsed")
    
    if step == "1. Basic Info":
        col1, col2 = st.columns(2)
        with col1:
            st.text_input("Full Name (as on PAN)")
            st.text_input("PAN Card Number")
        with col2:
            st.text_input("Mobile Number (Aadhaar linked)")
            st.text_input("Pincode")
        st.button("Continue to Income Check ➔")

    elif step == "2. Income Verification":
        col1, col2 = st.columns(2)
        with col1:
            st.selectbox("Employment Category", ["Salaried Employee", "Self-Employed / Business", "Gig Worker / Freelancer"])
            st.number_input("Monthly In-Hand Salary / Income (₹)", value=40000, step=5000)
        with col2:
            st.selectbox("Primary Bank Account", ["HDFC Bank", "ICICI Bank", "SBI", "Axis Bank", "Others"])
            st.file_uploader("Upload Last 3 Months Bank Statement (PDF)", type=["pdf"])
        st.button("Analyze & Fetch Best Offers 🚀")

    elif step == "3. Select Offer":
        st.success("🎉 Congratulations! You have 2 Pre-Approved Offers:")
        
        o1, o2 = st.columns(2)
        with o1:
            st.markdown("""
            <div class="metric-card" style="text-align: left; border-left: 4px solid #10B981;">
                <h4 style="color: #10B981; margin: 0;">Instant Micro-Loan</h4>
                <p style="font-size: 24px; font-weight: 800; margin: 10px 0;">Up to ₹50,000</p>
                <p style="color: #94A3B8; font-size: 13px;">• Disbursal in 5 mins<br>• Zero Processing Fee<br>• Flexible 6-month tenure</p>
            </div>
            """, unsafe_allow_html=True)
            st.write("")
            st.button("Claim Micro-Loan")
            
        with o2:
            st.markdown("""
            <div class="metric-card" style="text-align: left; border-left: 4px solid #6366F1;">
                <h4 style="color: #818CF8; margin: 0;">Flexi Personal Credit</h4>
                <p style="font-size: 24px; font-weight: 800; margin: 10px 0;">Up to ₹2,50,000</p>
                <p style="color: #94A3B8; font-size: 13px;">• Low monthly EMI<br>• Pay interest only on withdrawn amount<br>• Up to 36 months tenure</p>
            </div>
            """, unsafe_allow_html=True)
            st.write("")
            st.button("Claim Flexi Credit")

# ----------------------------------------------------
# TAB 3: Track Application Status
# ----------------------------------------------------
with tab3:
    st.subheader("Live Application Status")
    ref = st.text_input("Enter Reference ID or Mobile Number", value="TLW-88902")
    
    if st.button("Track Progress"):
        st.write("---")
        c_status, c_info = st.columns([1, 2])
        
        with c_status:
            st.markdown("""
            <div class="metric-card">
                <div class="metric-label">Status</div>
                <div style="color: #F59E0B; font-size: 22px; font-weight: 800; margin-top: 5px;">In Verification ⏳</div>
            </div>
            """, unsafe_allow_html=True)
            
        with c_info:
            st.info("Your bank statement analysis is complete. Our automated system is performing final KYC verification with your bank.")
            st.progress(75)
            st.caption("Step 3 of 4: Final Disbursal Approval in progress")