import React from "react";

export default function AgentStatus({ steps = [] }) {
  return (
    <div className="w-full p-4 bg-[#1f1f1f] border-t border-gray-800">

      <h3 className="text-sm text-gray-400 mb-3">
        Multi-Agent Pipeline
      </h3>

      <div className="space-y-2">
        {steps.map((step, idx) => (
          <div
            key={idx}
            className="flex justify-between text-sm"
          >
            <span>{step.name}</span>

            <span
              className={
                step.status === "done"
                  ? "text-green-400"
                  : step.status === "running"
                  ? "text-yellow-400 animate-pulse"
                  : "text-gray-500"
              }
            >
              {step.status}
            </span>
          </div>
        ))}
      </div>
    </div>
  );
}