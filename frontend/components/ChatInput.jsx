"use client";

import React, { useState } from "react";

export default function ChatInput({ onSend }) {
  const [text, setText] = useState("");

  const handleSend = () => {
    if (!text.trim()) return;
    onSend(text);
    setText("");
  };

  const handleKeyDown = (e) => {
    if (e.key === "Enter") {
      handleSend();
    }
  };

  return (
    <div className="w-full border-t border-gray-800 bg-[#1f1f1f] p-4 flex gap-2 items-center">
      
      <input
        value={text}
        onChange={(e) => setText(e.target.value)}
        onKeyDown={handleKeyDown}
        placeholder="Type your insurance claim..."
        className="flex-1 bg-[#2a2a2a] text-white px-4 py-3 rounded-xl outline-none"
      />

      <button
        onClick={handleSend}
        className="bg-[#10a37f] text-white px-5 py-2 rounded-lg"
      >
        Send
      </button>
    </div>
  );
}