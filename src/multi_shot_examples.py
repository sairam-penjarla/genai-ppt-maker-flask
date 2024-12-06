from src.prompt_templates import SLIDE_CONTENT_GUIDELINES

planning_examples = [
    {
        "role": "user",
        "content": 'what is LLM?'
    },
    {
        "role": "assistant",
        "content": """{ "slide_details": [ { "slide_number": 1, "purpose": "This slide serves as the introduction to the presentation on Large Language Models (LLMs). It should begin with a visually appealing title such as 'Introduction to Large Language Models.' Provide a brief overview of what LLMs are, emphasizing their role in Natural Language Processing (NLP). Mention how these models, trained on vast amounts of text data, are capable of understanding and generating human-like text. Briefly introduce their wide applications, such as chatbots, content generation, and language translation, setting the context for the deeper exploration in the following slides." }, { "slide_number": 2, "purpose": "This slide focuses on explaining the concept of Large Language Models (LLMs). Start by defining LLMs and describing how they function using deep learning techniques, specifically transformer architectures. Include a breakdown of the training process, where models learn from a vast corpus of text data. Explain their capacity to process, generate, and understand language at scale. Provide examples of popular LLMs, such as GPT-3 and BERT, and highlight their capabilities. End with a discussion on the significance of LLMs in advancing NLP tasks." }, { "slide_number": 3, "purpose": "This slide delves deeper into the applications of Large Language Models. Discuss the diverse range of tasks LLMs can perform, including but not limited to text generation, translation, summarization, and sentiment analysis. Provide specific examples of how these applications are utilized in industries like customer service, content creation, and healthcare. Highlight the impact LLMs have had in automating complex language tasks and their ability to understand context, tone, and nuances in language." }, { "slide_number": 4, "purpose": "This slide provides an overview of the challenges and limitations associated with Large Language Models. Discuss issues such as computational resources required for training, the need for large annotated datasets, and concerns around model bias and ethical implications. Address limitations in handling specialized or domain-specific knowledge, and highlight the potential for overfitting or undesirable outputs. Provide examples of challenges in using LLMs in real-world applications, emphasizing the importance of fine-tuning and model optimization." }, { "slide_number": 5, "purpose": "This slide serves as the conclusion and key takeaways. Summarize the key points covered in the presentation, reiterating the capabilities, applications, and challenges of Large Language Models. Discuss their future potential, including advancements in hybrid models and improvements in efficiency. Provide recommendations on the use of LLMs in different NLP tasks, depending on the scale of data and available resources. Conclude with a forward-looking statement on how LLMs will continue to evolve and shape the future of NLP and AI." } ] }"""
    },
    {
        "role": "user",
        "content": "What is the status of the current project?"
    },
    {
        "role": "assistant",
        "content": """{
            "slide_details": [
                {
                    "slide_number": 1,
                    "purpose": "This slide serves as an introduction to the current project's status. It should provide an overview of the project objectives, current milestones, and key deliverables. Mention the project's timeline and any critical deadlines. Briefly introduce the team and stakeholders involved, and provide context on the project's significance and its impact on business goals."
                },
                {
                    "slide_number": 2,
                    "purpose": "This slide outlines the progress made on the project so far. Discuss completed tasks, milestones achieved, and any deliverables that have been submitted. Include visuals such as a Gantt chart or progress bar to illustrate the timeline and work done. Highlight any success stories or achievements that stand out and show how the team has met deadlines or surpassed expectations."
                },
                {
                    "slide_number": 3,
                    "purpose": "This slide focuses on identifying any challenges or roadblocks encountered during the project. Discuss issues such as resource constraints, unexpected delays, or technical difficulties. Include a problem-solving approach and steps taken to address these challenges. If relevant, suggest potential solutions or adjustments that may be necessary moving forward."
                },
                {
                    "slide_number": 4,
                    "purpose": "This slide outlines the next steps for the project. Focus on the upcoming tasks, timelines, and expectations. Mention any upcoming milestones or deadlines that the team is working towards. Include a clear action plan and assign responsibilities to specific team members. Highlight the support or resources needed to ensure the continued success of the project."
                },
                {
                    "slide_number": 5,
                    "purpose": "This slide serves as the conclusion, summarizing the overall status of the project. Provide a high-level summary of achievements, challenges, and next steps. Reiterate any key decisions made during the status update, and make sure the team and stakeholders are aligned on future priorities. Conclude with any open questions or requests for additional resources or support."
                }
            ]
        }"""
    },
    {
        "role": "user",
        "content": "How can AI improve customer experience in healthcare?"
    },
    {
        "role": "assistant",
        "content": """{
            "slide_details": [
                {
                    "slide_number": 1,
                    "purpose": "This slide introduces the topic of improving customer experience in healthcare using AI. The title could be 'Leveraging AI to Enhance Customer Experience in Healthcare.' Provide a brief overview of the current state of customer experience in healthcare and the growing importance of patient-centered care. Mention the role AI can play in transforming the patient experience by providing personalized, efficient, and accessible healthcare services."
                },
                {
                    "slide_number": 2,
                    "purpose": "This slide explores various AI applications in healthcare that contribute to customer experience. Discuss AI-powered chatbots and virtual assistants for answering patient queries, appointment scheduling, and triaging symptoms. Include examples of AI-driven systems like symptom checkers and patient-facing apps that enable quick and accurate responses. Mention AI in diagnostics, helping physicians make faster and more accurate decisions, leading to improved patient satisfaction."
                },
                {
                    "slide_number": 3,
                    "purpose": "This slide focuses on AI-based personalization in healthcare. Discuss how AI can help create personalized treatment plans by analyzing patient data, including medical history, preferences, and genetic information. Explore the role of recommendation systems in suggesting lifestyle changes, medications, or healthcare services based on individual patient needs. Highlight the benefits of personalized care in increasing patient engagement and satisfaction."
                },
                {
                    "slide_number": 4,
                    "purpose": "This slide addresses the challenges and limitations of implementing AI in healthcare. Discuss issues such as data privacy concerns, integration with existing healthcare systems, and the need for quality, labeled data. Explore the barriers to adoption from both healthcare providers and patients, such as resistance to change, lack of trust in AI, and regulatory constraints. Include real-world examples of challenges faced in AI implementations."
                },
                {
                    "slide_number": 5,
                    "purpose": "This slide concludes the presentation, summarizing the key takeaways about AI's impact on healthcare customer experience. Recap the main points regarding AI's ability to enhance personalization, improve service delivery, and streamline healthcare processes. Offer a forward-looking perspective, emphasizing the potential for further innovations in AI and healthcare to address evolving patient needs and improve overall care quality."
                }
            ]
        }"""
    },
    {
        "role": "user",
        "content": "Can you propose a business solution for supply chain optimization?"
    },
    {
        "role": "assistant",
        "content": """{
            "slide_details": [
                {
                    "slide_number": 1,
                    "purpose": "This slide serves as the introduction to a proposed solution for supply chain optimization. The title could be 'Optimizing Supply Chain Management with Advanced Technologies.' Provide a brief overview of the supply chain process and the challenges that businesses face, such as delays, high costs, and inventory mismanagement. Introduce the solution, mentioning how it integrates advanced technologies like AI, machine learning, and IoT to improve supply chain efficiency."
                },
                {
                    "slide_number": 2,
                    "purpose": "This slide outlines the key pain points in the current supply chain that the proposed solution addresses. Discuss issues such as demand forecasting inaccuracies, delayed shipments, lack of real-time data, and high operational costs. Use visuals such as charts or graphs to highlight the impact of these problems on business operations. Explain why current methods are insufficient and why the proposed solution is needed."
                },
                {
                    "slide_number": 3,
                    "purpose": "This slide presents the core elements of the proposed business solution. Discuss how AI-powered predictive analytics can enhance demand forecasting accuracy and optimize inventory management. Highlight the role of machine learning algorithms in route optimization and real-time shipment tracking using IoT sensors. Describe the benefits of automation in warehousing and order fulfillment processes. Provide a high-level overview of how these technologies can work together to streamline the supply chain."
                },
                {
                    "slide_number": 4,
                    "purpose": "This slide addresses the implementation strategy for the solution. Discuss the steps needed to adopt the proposed technologies, including pilot testing, integration with existing systems, and training employees. Mention the timeline and milestones for each phase of the implementation, as well as any key considerations such as cost, resource allocation, and potential risks. Highlight how the solution will be scaled across the organization."
                },
                {
                    "slide_number": 5,
                    "purpose": "This slide concludes the proposal, summarizing the expected outcomes and benefits of the solution. Discuss how the implementation of the proposed supply chain optimization technologies will reduce costs, improve efficiency, and enhance customer satisfaction. Provide a future outlook on how these technologies can evolve and further improve the supply chain process over time. End with a call to action or recommendation for the next steps in implementing the solution."
                }
            ]
        }"""
    },
    {
        "role": "user",
        "content": "How can I improve employee engagement in my company?"
    },
    {
        "role": "assistant",
        "content": """{
            "slide_details": [
                {
                    "slide_number": 1,
                    "purpose": "This slide introduces the topic of employee engagement and why it is important for company success. The title could be 'Strategies for Improving Employee Engagement.' Provide a brief overview of the link between engaged employees and business outcomes such as productivity, retention, and morale. Mention the need for a strategic approach to fostering engagement across all levels of the organization."
                },
                {
                    "slide_number": 2,
                    "purpose": "This slide focuses on understanding the current state of employee engagement in your company. Discuss how employee engagement is measured through surveys, feedback sessions, and performance reviews. Share insights from recent data or employee feedback, highlighting areas that need improvement. Address common issues such as lack of recognition, unclear career paths, or low job satisfaction."
                },
                {
                    "slide_number": 3,
                    "purpose": "This slide presents strategies for improving employee engagement. Discuss the importance of recognition programs, career development opportunities, and work-life balance initiatives. Highlight how clear communication and transparency from leadership can foster a sense of trust and loyalty among employees. Include specific examples of successful initiatives, such as mentorship programs or team-building activities."
                },
                {
                    "slide_number": 4,
                    "purpose": "This slide discusses the role of technology in improving employee engagement. Explore the use of engagement platforms and internal communication tools that facilitate feedback, collaboration, and recognition. Mention how data analytics can be used to track employee sentiment and engagement levels in real-time, allowing for timely interventions. Include examples of tools or platforms your company can leverage."
                },
                {
                    "slide_number": 5,
                    "purpose": "This slide concludes with the expected outcomes and next steps for improving employee engagement. Recap the key strategies and technologies discussed in the presentation. Outline a clear action plan for implementing these initiatives, including timelines and responsibilities. Conclude with a call to action, encouraging leadership to prioritize employee engagement as part of the company's overall strategy for growth and success."
                }
            ]
        }"""
    },
    {
        "role": "user",
        "content": "Can you give a status update on the healthcare project?"
    },
    {
        "role": "assistant",
        "content": """{
            "slide_details": [
                {
                    "slide_number": 1,
                    "purpose": "This slide introduces the healthcare project's current status. The title could be 'Healthcare Project Status Update.' Provide a brief overview of the project's goals, such as improving patient care or optimizing healthcare operations. Mention the stakeholders involved and any  key objectives or milestones for the project."
                },
                {
                    "slide_number": 2,
                    "purpose": "This slide focuses on progress made so far in the healthcare project. Discuss completed tasks, such as data collection, model development, or system integration. Use visuals such as progress bars or charts to illustrate work completed compared to the planned timeline. Highlight any major accomplishments, such as successful pilot testing or stakeholder buy-in."
                },
                {
                    "slide_number": 3,
                    "purpose": "This slide identifies challenges encountered during the project. Discuss technical hurdles, such as data privacy concerns, regulatory requirements, or integration with existing healthcare systems. Highlight any resource limitations or unexpected delays. If applicable, mention steps taken to resolve these issues and mitigate risks."
                },
                {
                    "slide_number": 4,
                    "purpose": "This slide outlines the next steps for the project. Focus on upcoming tasks, such as finalizing the development phase, conducting more tests, or rolling out the solution. Mention key deadlines, any pending approvals, and who is responsible for each task. Emphasize how these steps align with the overall project goals."
                },
                {
                    "slide_number": 5,
                    "purpose": "This slide concludes with a summary of the project's status. Recap the progress made, challenges faced, and next steps. Reinforce the importance of the project for healthcare outcomes, and remind stakeholders of the expected impact once completed. Provide a call to action for any additional resources or decisions needed to keep the project on track."
                }
            ]
        }"""
    }
]


content_examples = [
    {
      "role": "user",
      "content": """This slide focuses on progress made so far in the healthcare project. Discuss completed tasks, such as data collection, model development, or system integration. Use visuals such as progress bars or charts to illustrate work completed compared to the planned timeline. Highlight any major accomplishments, such as successful pilot testing or stakeholder buy-in."""
    },
    {
      "role": "assistant",
      "content": """{\n  \"slides\": [\n    {\n      \"titles\": {\n        \"slide_title\": \"Healthcare Project Progress\",\n        \"long_title\": \"Tracking Progress in the Healthcare Project\",\n        \"sub_title\": \"Status and Key Accomplishments\"\n      },\n      \"content\": [\n        {\n          \"heading\": \"Data Collection Complete\",\n          \"content\": \"All data collection phases have been successfully completed, with the required datasets gathered from hospitals and health institutions. This forms the foundation for model development and further analysis.\"\n        },\n        {\n          \"heading\": \"Model Development Underway\",\n          \"content\": \"The machine learning models for healthcare predictions are being trained. Several prototypes have been developed and are in the evaluation phase to assess their performance.\"\n        },\n        {\n          \"heading\": \"System Integration Progress\",\n          \"content\": \"The integration of various healthcare systems has been progressing smoothly. APIs are being tested for real-time data exchange between systems and the model, with preliminary success in pilot integrations.\"\n        },\n        {\n          \"heading\": \"Pilot Testing Achieved\",\n          \"content\": \"Pilot testing has been successfully conducted with a select group of healthcare providers. The feedback has been overwhelmingly positive, validating the model's effectiveness in real-world scenarios.\"\n        },\n        {\n          \"heading\": \"Stakeholder Buy-In Secured\",\n          \"content\": \"Key stakeholders have expressed their approval and confidence in the project's direction. Meetings with stakeholders confirmed the alignment of the project's goals with the broader healthcare objectives.\"\n        }\n      ]\n    }\n  ]\n}"""
    },
    {
      "role": "user",
      "content": """This slide introduces the healthcare project's current status. The title could be 'Healthcare Project Status Update.' Provide a brief overview of the project's goals, such as improving patient care or optimizing healthcare operations. Mention the stakeholders involved and any key objectives or milestones for the project."""
    },
    {
      "role": "assistant",
      "content": """{\n  \"slides\": [\n    {\n      \"titles\": {\n        \"slide_title\": \"Healthcare Project Status Update\",\n        \"long_title\": \"Current Status of Healthcare Project\",\n        \"sub_title\": \"Key Goals, Objectives, and Stakeholders\"\n      },\n      \"content\": [\n        {\n          \"heading\": \"Project Goals\",\n          \"content\": \"The goal of this project is to improve patient care by leveraging AI and machine learning for predictive analytics, while also optimizing healthcare operations to increase efficiency and reduce costs.\"\n        },\n        {\n          \"heading\": \"Stakeholders Involved\",\n          \"content\": \"The project involves a collaboration between healthcare providers, data scientists, technology developers, and regulatory bodies. Key stakeholders include healthcare institutions, government health agencies, and research organizations.\"\n        },\n        {\n          \"heading\": \"Key Milestones\",\n          \"content\": \"The key objectives include finalizing data collection, completing model development, integrating the solution into existing systems, and conducting pilot testing. The first pilot phase is expected to be completed within three months.\"\n        }\n      ]\n    }\n  ]\n}"""
    },
    {
      "role": "user",
      "content": """This slide addresses the implementation strategy for the solution. Discuss the steps needed to adopt the proposed technologies, including pilot testing, integration with existing systems, and training employees."""
    },
    {
      "role": "assistant",
      "content": """{\n  \"slides\": [\n    {\n      \"titles\": {\n        \"slide_title\": \"Implementation Strategy\",\n        \"long_title\": \"Strategic Approach for Implementing the Healthcare Solution\",\n        \"sub_title\": \"Steps for Adoption and Integration\"\n      },\n      \"content\": [\n        {\n          \"heading\": \"Pilot Testing\",\n          \"content\": \"Initial testing will be conducted in a controlled environment, focusing on a small set of healthcare providers. This phase will help identify any challenges and provide real-world feedback on system functionality.\"\n        },\n        {\n          \"heading\": \"System Integration\",\n          \"content\": \"The solution will be integrated with existing healthcare management systems. This includes connecting APIs for data exchange and ensuring compatibility with electronic health records (EHRs) and other legacy systems.\"\n        },\n        {\n          \"heading\": \"Employee Training\",\n          \"content\": \"A comprehensive training program will be rolled out to healthcare professionals and administrative staff. This training will cover how to use the new system effectively, ensuring smooth adoption.\"\n        }\n      ]\n    }\n  ]\n}"""
    },
    {
      "role": "user",
      "content": """This slide focuses on the next steps for the healthcare project. Discuss upcoming tasks, such as finalizing the development phase, conducting more tests, or rolling out the solution."""
    },
    {
      "role": "assistant",
      "content": """{\n  \"slides\": [\n    {\n      \"titles\": {\n        \"slide_title\": \"Next Steps for Healthcare Project\",\n        \"long_title\": \"Planning the Next Phases of the Healthcare Project\",\n        \"sub_title\": \"Development, Testing, and Rollout\"\n      },\n      \"content\": [\n        {\n          \"heading\": \"Finalizing Development\",\n          \"content\": \"The final development phase will involve refining the machine learning models, enhancing system functionality, and conducting stress tests to ensure scalability and robustness.\"\n        },\n        {\n          \"heading\": \"Expanding Testing Phases\",\n          \"content\": \"Additional testing will be carried out with a larger group of healthcare providers to validate the solution's performance across diverse settings. Further fine-tuning will be done based on feedback.\"\n        },\n        {\n          \"heading\": \"Solution Rollout\",\n          \"content\": \"The solution will be rolled out across all partner healthcare institutions, with full deployment expected by the end of the quarter. This will include continued support and monitoring for early-stage adoption.\"\n        }\n      ]\n    }\n  ]\n}"""
    },
    {
      "role": "user",
      "content": """This slide concludes the proposal, summarizing the expected outcomes and benefits of the solution. Discuss how the implementation of the proposed supply chain optimization technologies will reduce costs, improve efficiency, and enhance customer satisfaction."""
    },
    {
      "role": "assistant",
      "content": """{\n  \"slides\": [\n    {\n      \"titles\": {\n        \"slide_title\": \"Conclusion and Key Benefits\",\n        \"long_title\": \"Summarizing the Impact of Supply Chain Optimization\",\n        \"sub_title\": \"Expected Outcomes of the Proposed Solution\"\n      },\n      \"content\": [\n        {\n          \"heading\": \"Cost Reduction\",\n          \"content\": \"The implementation of AI-driven predictive analytics and optimization technologies will lead to significant cost savings by reducing waste, improving inventory management, and minimizing delays.\"\n        },\n        {\n          \"heading\": \"Efficiency Gains\",\n          \"content\": \"By automating key supply chain processes, the solution will streamline operations, increase throughput, and ensure on-time deliveries. This will improve overall operational efficiency.\"\n        },\n        {\n          \"heading\": \"Enhanced Customer Satisfaction\",\n          \"content\": \"Faster and more reliable delivery of products will enhance customer satisfaction by improving service quality. Customers will benefit from a more responsive supply chain, with better tracking and predictability.\"\n        }\n      ]\n    }\n  ]\n}"""
    }
]



def get_exmaples(component):
    if component == SLIDE_CONTENT_GUIDELINES:
        return content_examples
    else:
        return planning_examples