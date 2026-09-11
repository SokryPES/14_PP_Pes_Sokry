# Test Log: Naive RAG System Evaluation
**System Parameters:**
- **Embedding Model:** `nomic-embed-text`
- **Generation Model:** `llama3.2`
- **Chunk Size / Overlap:** 800 / 120
- **Top K:** 4

---

# Test 1: General Document Overview (In Topic)
- **Question:** "What are these documents about?"
- **Retrieved Sources:**
  - `003_Configuring_VPN_Access_for_Remote_Workers.txt`
  - `004_Troubleshooting_Issues_with_Microsoft_Office.txt`
  - `006_Creating_a_Backup_of_Important_Files.txt`
- **Generated Answer:** 
  > These documents are about creating a backup of important files and configuring VPN access for remote workers, as well as troubleshooting issues with Microsoft Office. Specifically, they cover topics such as identifying important files, choosing a backup method, and configuring VPN access, as well as troubleshooting common issues with Microsoft Office applications.

---

# Test 2: Microsoft Office Troubleshooting Overview (In Topic)
- **Question:** "What are the common symptoms or problems that happen with Microsoft Office?"
- **Retrieved Sources:**
  - `004_Troubleshooting_Issues_with_Microsoft_Office.txt`
- **Generated Answer:** 
  > The context does not specifically mention the common symptoms or problems that happen with Microsoft Office, but rather provides steps to troubleshoot common issues with Microsoft Office applications. However, it does mention that the issue "can sometimes cause problems" and that "some antivirus programs can interfere with Microsoft Office applications".

---

# Test 2: Backup Storage Methods (In Topic)
- **Question:** "What are the available storage methods for backing up important files?"
- **Retrieved Sources:**
  - `006_Creating_a_Backup_of_Important_Files.txt`
- **Generated Answer:** 
  > The available storage methods for backing up important files are:
  > * External Hard Drive
  > * Cloud Backup
  > * Backup Location (Note: this is not a specific storage method, but rather a general term for storing the backup device in a safe location)
  > * USB Drive
  > These are the methods mentioned in the context provided.

---

# Test 3: VPN Connection Prerequisites (In Topic)
- **Question:** "what are the key prerequisites needed to establish a VPN connection for remote work?"
- **Retrieved Sources:**
  - `003_Configuring_VPN_Access_for_Remote_Workers.txt`
- **Generated Answer:** 
  > According to the context, the key prerequisites needed to establish a VPN connection for remote work are:
  > 1. The remote worker's device (laptop or desktop) must meet the company's minimum system requirements for VPN connectivity.
  > 2. The remote worker must have a valid company login credentials.
  > 3. The remote worker must have a stable internet connection.

---

# Test 4: Remote Work Expense Policy (Out of Topic)
- **Question:** "What is the company policy regarding remote work reimbursement for office furniture?"
- **Retrieved Sources:**
  - `001_Setting_Up_a_Mobile_Device_for_Company_Email.txt`
  - `003_Configuring_VPN_Access_for_Remote_Workers.txt`
  - `004_Troubleshooting_Issues_with_Microsoft_Office.txt`
- **Generated Answer:** 
  > I don't have enough information in the documents to answer that.

--- 

# Test 5: General World Knowledge (Out of Topic)
- **Question:** "What is the capital city of cambodia?"
- **Retrieved Sources:**
  - `003_Configuring_VPN_Access_for_Remote_Workers.txt`
  - `005_Setting_Up_a_Conference_Call_on_Cisco_Webex.txt`
  - `006_Creating_a_Backup_of_Important_Files.txt`
- **Generated Answer:** 
  > I don't have enough information in the documents to answer that.
