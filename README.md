# Teh Ro-Vin | AI Automation Portfolio

I build AI-assisted applications that connect language models with practical workflows, authenticated tools and business systems. My work combines application development, agent orchestration, integration and structured evaluation.

This showcase presents two selected projects from my resume. Their full source repositories remain private; the descriptions below focus on the work I can discuss in a technical walkthrough.

## Lumen Property Management System

A property management platform that brings together tenant, lease, rent payment, expense and maintenance information, with AI-assisted workflows for owners and tenants.

**Selected automation and integration work**

- Built a tool-calling owner assistant and MCP server to answer portfolio questions and propose record changes, with organisation-scoped access and owner approval.
- Integrated WhatsApp rent enquiries and Stripe payment evidence into a landlord review workflow, keeping payment claims separate from approved payment records.
- Developed a Telegram voice assistant using Gemini Live and a Python audio bridge to collect maintenance reports, verify tenant context and request confirmation before ticket submission.

**Technology:** TypeScript, Next.js, NestJS, Supabase/PostgreSQL, MCP, Python, Gemini Live and external messaging/payment integrations.

**Demonstration:** The Telegram voice flow was tested. The WhatsApp payment workflow was recorded on video during its service trial; live availability depends on third-party services.

## UTAR Sport Facility | Individual Final-Year Project

An application for sports facility booking, payment workflows, matchmaking and recommendations, with an AI assistant that uses authenticated tools and user-scoped memory.

**Selected AI and automation work**

- Built the application with React Native/Expo and Firebase, and developed a Python/FastAPI agent using LangGraph.
- Connected the agent to authenticated tools and booking workflows, with user confirmation before a booking action.
- Implemented persistent user-scoped memory and hybrid retrieval-augmented generation, then used self-hosted Langfuse on Docker to track evaluations and traces.

**Controlled memory evaluation**

| Metric | Result |
| --- | --- |
| Memory selection precision | 80.95% (17 / 21 selected items relevant) |
| Target-memory hit@3 | 16 / 16 positive queries |
| Micro recall and micro-F1 | 100% and 89.47%, respectively |
| Memory-write authorisation checks | 14 / 14 passed |

These figures come from a small, controlled offline evaluation. They describe the tested cases and should not be interpreted as production accuracy or real-world user outcomes. See the [evaluation method and limitations](evaluation/memory-selection.md).

**Technology:** Python, FastAPI, LangGraph, LangChain, React Native, Expo, Firebase, Langfuse and Docker.

## How I approach AI automation

I focus on understanding the underlying workflow, connecting tools through clear interfaces, validating inputs and permissions, and measuring how the system behaves. Where an action can change a record or submit a request, I use explicit confirmation or a review step appropriate to the workflow.

Project walkthroughs and demonstrations can be discussed on request. Full source code is not published in this showcase.
