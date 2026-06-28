
"use client";

import React, { useState } from "react";
import MessageBubble from "./MessageBubble";
import ChatInput from "./ChatInput";
import UploadArea from "./UploadArea";
import AgentStatus from "./AgentStatus";
import ReportCard from "./ReportCard";
import { sendMessage, uploadImages } from "../lib/api";
export default function ChatWindow() {
  const [messages, setMessages] = useState([
    {
      role: "assistant",
      text: "Hi! I am your Insurance Claim AI Agent. Describe your claim to begin."
    }
  ]);

  const [loading, setLoading] = useState(false);
  const [showUpload, setShowUpload] = useState(false);
  const [agentSteps, setAgentSteps] = useState([]);
  const [report, setReport] = useState(null);

 const [currentMessage, setCurrentMessage] = useState("");

const handleSend = async (text) => {
  setCurrentMessage(text);

  setMessages((prev) => [
    ...prev,
    {
      role: "user",
      text,
    },
  ]);

  setLoading(true);
  setReport(null);
  setAgentSteps([]);

  try {
    const data = await sendMessage(text);

    setMessages((prev) => [
      ...prev,
      {
        role: "assistant",
        text:
          data.reply ||
          "Please upload images of the damage.",
      },
    ]);

    setShowUpload(true);
  } catch (err) {
    setMessages((prev) => [
      ...prev,
      {
        role: "assistant",
        text: "Unable to reach backend.",
      },
    ]);
  }

  setLoading(false);
};

  const handleUpload = async (files) => {
  setShowUpload(false);

  setAgentSteps([
    { name: "Conversation Agent", status: "done" },
    { name: "Image Agent", status: "running" },
    { name: "Evidence Agent", status: "pending" },
    { name: "History Agent", status: "pending" },
    { name: "Decision Agent", status: "pending" },
  ]);

  try {
    const result = await uploadImages(
      files,
      currentMessage
    );

    setAgentSteps([
      { name: "Conversation Agent", status: "done" },
      { name: "Image Agent", status: "done" },
      { name: "Evidence Agent", status: "done" },
      { name: "History Agent", status: "done" },
      { name: "Decision Agent", status: "done" },
    ]);

    setReport({
  status: result.final.claim_status,
  object: result.final.claim_object,
  issue: result.final.issue_type,
  part: result.final.object_part,
  severity: result.final.severity,
  reason: result.final.claim_status_justification,
});

    setMessages((prev) => [
      ...prev,
      {
        role: "assistant",
        text: "Analysis completed successfully.",
      },
    ]);
  } catch (err) {
    setMessages((prev) => [
      ...prev,
      {
        role: "assistant",
        text: "Image analysis failed.",
      },
    ]);
  }
};

  return (
    <div className="flex flex-col h-screen w-full bg-[#212121]">

      {/* Messages */}
      <div className="flex-1 overflow-y-auto p-6 space-y-4">

        {messages.map((msg, index) => (
          <MessageBubble key={index} message={msg} />
        ))}

        {loading && (
          <div className="text-gray-400 text-sm animate-pulse">
            Insurance AI is analyzing your request...
          </div>
        )}

        {/* Agent Pipeline */}
        {agentSteps.length > 0 && (
          <AgentStatus steps={agentSteps} />
        )}

        {/* Final Report */}
        {report && (
          <ReportCard data={report} />
        )}
      </div>

      {/* Upload Area */}
      {showUpload && (
        <UploadArea onUpload={handleUpload} />
      )}

      {/* Input */}
      <ChatInput onSend={handleSend} />
    </div>
  );
}