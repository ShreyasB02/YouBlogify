
# YouBlogify 🎥→✍️  
**Transform YouTube Videos into High-Quality Blogs using AWS + LLMs + LangChain + CREW AI**

## 🚀 Overview

**YouBlogify** is an end-to-end GenAI application that leverages AWS Bedrock, CREW AI, and LangChain to automatically convert YouTube video content into insightful, SEO-friendly blog posts.  
The system is fully serverless, scalable, and production-ready — making it a perfect blueprint for deploying intelligent media automation solutions.

---

## 🧠 Features

- ✅ Converts any YouTube video into a structured blog post.
- 🤖 Powered by **LLMs from AWS Bedrock** (Claude-v2).
- 🧩 Modular agent-based architecture using **CREW AI**.
- 📦 LangChain-powered pipelines for LLM orchestration.
- ☁️ Deployed using **AWS Lambda**, **API Gateway**, and **S3**.
- 🔐 Serverless, cost-efficient, and highly scalable.

---

## 📸 System Architecture

```
User Input (YouTube URL / Topic)
        |
        v
API Gateway (POST /generate-blog)
        |
        v
AWS Lambda:
   - Extracts Video Transcript (or Topic)
   - Initiates CREW AI Agent Pipeline
        |
        v
CREW AI Agents:
   1. **Research Agent**: Summarizes key points.
   2. **Writer Agent**: Creates a structured blog post.
   3. **Refiner Agent**: Edits and enhances content.
        |
        v
AWS Bedrock (Claude-v2)
        |
        v
LangChain Output Parsing
        |
        v
Blog Stored in S3 Bucket
```

---

## 🛠️ Tech Stack

| Layer               | Technology Used                             |
|---------------------|---------------------------------------------|
| 🧠 LLM               | Claude-v2 via AWS Bedrock                   |
| 🤖 Agent Orchestration | CREW AI, LangChain                        |
| 🧱 Infrastructure    | AWS Lambda, S3, API Gateway                 |
| 🔗 Backend Framework | FastAPI / Flask (Locally)                  |
| 🎥 Input             | YouTube Transcript or Topic Prompt         |

---

## 🧪 Evaluation Metrics

- **Factual Accuracy** (manual audit / GPT-assisted QA).
- **Readability** (Flesch-Kincaid / Hemingway App).
- **Coherence Score** (BERTScore / BLEU for long-form).
- **User Engagement** (CTR on blog vs. video).
- **Latency** (end-to-end inference time).

---

## 📦 Installation & Deployment

### 🔧 Local Dev Setup

```bash
git clone https://github.com/yourname/youblogify.git
cd youblogify
pip install -r requirements.txt
```

### 🧪 Test locally

```bash
python app.py  # For Flask or FastAPI app
```

### ☁️ Deploy on AWS

1. Package the Lambda function:
   ```bash
   zip -r function.zip .
   ```
2. Create a Lambda function (Python 3.10) and upload the ZIP.
3. Attach execution role with S3 + Bedrock + Logs access.
4. Set up API Gateway to trigger the Lambda via POST.
5. Point the frontend/client to your API endpoint.

---

## 📥 API Usage

### Endpoint

```
POST /generate-blog
```

### Payload

```json
{
  "topic": "How Generative AI is Transforming Healthcare"
}
```

### Response

```json
{
  "blog_url": "https://yourbucket.s3.amazonaws.com/generated_blogs/blog123.html"
}
```

---

## 📌 Future Enhancements

- [ ] Integrate image generation for visual blogs.
- [ ] Add multi-language blog support.
- [ ] YouTube transcription via Whisper + LangChain.
- [ ] Integrate real-time monitoring with AWS CloudWatch.

---

## 🤝 Collaborators

| Name         | Role                 |
|--------------|----------------------|
| Shreyas Battula | Developer, Architect |
| AWS Bedrock | LLM Service Provider |
| LangChain & CREW AI | Core Frameworks |

---

## 🧾 License

MIT License. See [LICENSE](LICENSE) for details.

---

## 💡 Inspiration

The idea for YouBlogify was inspired by the need for automated, scalable content generation from high-value media like lectures, interviews, and podcasts.

---

## 📬 Contact

For any inquiries or collaborations, reach out to  
📧 **shreyasbattula152002@gmail.com**  

---
