import streamlit as st
import re

st.set_page_config(
    page_title="APEX | Cloud Intelligence Platform",
    page_icon="◼️",
    layout="wide"
)

st.title("◼️ APEX")
st.subheader("Intelligent Cloud Cost, Security & Operations Platform")
st.markdown("**Built by Harshitha | Problem:** Startups lose 30% cloud budget to idle servers, leaked secrets and crash errors.")
st.divider()

tab1, tab2, tab3, tab4 = st.tabs(["COST ANALYSIS", "RESOURCE TRACKER", "FAILURE DIAGNOSIS", "SECURITY SCAN"])

with tab1:
    st.subheader("Module 1: Cost Analysis Engine")
    st.write("Detects idle infrastructure wasting budget.")
    c1, c2 = st.columns(2)
    with c1:
        cpu = st.slider("CPU Utilization %", 0, 100, 5)
    with c2:
        hours = st.slider("Hours Running", 1, 24, 10)
    if st.button("Run Cost Analysis", type="primary"):
        if cpu < 20 and hours > 5:
            waste = hours * 0.12 * 30
            st.error(f"WASTE DETECTED: {cpu}% utilization for {hours} hours")
            st.metric("Estimated Monthly Waste", f"${waste:.2f}", f"Rs {waste*83:.0f}")
        else:
            st.success("Optimal utilization. No waste detected.")

with tab2:
    st.subheader("Module 2: Resource Tracker")
    st.write("Measures compute consumption and efficiency.")
    lines = st.number_input("Number of Executions", 100, 1000000, 1000)
    if st.button("Calculate Consumption"):
        units = lines * 0.00012
        st.warning(f"Consumption: {units:.4f} units")
        st.info("Optimization: Schedule heavy workloads during low-load windows for 40% efficiency gain.")

with tab3:
    st.subheader("Module 3: Failure Diagnosis")
    st.write("Translates complex infrastructure logs into actionable fixes.")
    log = st.text_area("Paste Infrastructure Log", "OOMKilled - Exit Code 137", height=100)
    if st.button("Diagnose Failure"):
        l = log.lower()
        if "137" in l or "oom" in l:
            st.error("DIAGNOSIS: Out Of Memory Failure")
            st.markdown("**Root Cause:** Application memory limit exceeded.")
            st.code("Resolution: Increase memory allocation: 512Mi -> 1Gi in deployment.yaml")
        elif "crashloop" in l:
            st.error("DIAGNOSIS: CrashLoopBackOff - Continuous Crash")
            st.code("Resolution: kubectl logs <pod-name> --previous")
        elif "imagepull" in l:
            st.error("DIAGNOSIS: ImagePullBackOff - Image Not Found")
            st.code("Resolution: Verify image name and registry push")
        else:
            st.info("Run detailed log analysis.")

with tab4:
    st.subheader("Module 4: Security Scan")
    st.write("Prevents credential leakage before production push.")
    code = st.text_area("Paste Code for Scan", 'aws_key = "AKIAIOSFODNN7EXAMPLE"', height=150)
    if st.button("Run Security Scan", type="primary"):
        found = re.findall(r'AKIA[0-9A-Z]{16}|password\s*=\s*["\'].*["\']|api_key\s*=\s*["\'].*["\']', code, re.IGNORECASE)
        if found:
            st.error(f"CRITICAL: {len(found)} Exposed Credential(s) Detected")
            st.code(str(found))
            st.warning("Action Required: Remove credentials before push.")
        else:
            st.success("Scan Clear. No credentials detected. Safe to deploy.")

st.divider()
st.caption("APEX | Built by Harshitha | Python, Streamlit, FinOps, SecOps")
