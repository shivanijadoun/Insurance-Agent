import React from "react";

export default function ReportCard({ data }) {
  if (!data) return null;

  return (
    <div className="w-full p-4 bg-[#1f1f1f] border border-gray-800 rounded-xl mt-4">

      <h2 className="text-lg font-semibold text-white mb-3">
        Claim Verification Report
      </h2>

      {/* Status */}
      <div className="mb-2">
        <span className="text-gray-400">Status: </span>
        <span
          className={
            data.status === "supported"
              ? "text-green-400"
              : data.status === "contradicted"
              ? "text-red-400"
              : "text-yellow-400"
          }
        >
          {data.status?.toUpperCase()}
        </span>
      </div>

      <p className="text-sm text-gray-300">
        <b>Object:</b> {data.object}
      </p>

      <p className="text-sm text-gray-300">
        <b>Issue:</b> {data.issue}
      </p>

      <p className="text-sm text-gray-300">
        <b>Part:</b> {data.part}
      </p>

      <p className="text-sm text-gray-300">
        <b>Severity:</b> {data.severity}
      </p>

      <div className="mt-3 text-sm text-gray-400">
        {data.reason}
      </div>
    </div>
  );
}