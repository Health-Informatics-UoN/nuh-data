module.exports = {
  branches: ["main"],
  tagFormat: "${version}",
  preset: "angular",
  repositoryUrl: "https://github.com/Health-Informatics-UoN/nuh-data.git",
  plugins: [
    "@semantic-release/commit-analyzer",
    "@semantic-release/release-notes-generator",
    "@semantic-release/exec",
    [
      "@semantic-release/github",
      {
        // Publish as a draft first. GitHub's immutable releases make a published
        // release read-only, so the datadict job's asset upload (release.yml) would
        // fail against an already-published release. action-gh-release publishes
        // (un-drafts) the release itself once the CSVs are attached.
        draftRelease: true,
      },
    ],
  ],
};
