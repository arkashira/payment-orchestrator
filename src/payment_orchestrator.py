import json
from dataclasses import dataclass
from enum import Enum
from typing import List

class IssueStatus(Enum):
    DETECTED = "detected"
    RESOLVED = "resolved"

@dataclass
class Issue:
    id: int
    description: str
    resolution_steps: List[str]
    status: IssueStatus

class PaymentOrchestrator:
    def __init__(self):
        self.issues = []
        self.clients = []

    def add_client(self, client_id: int):
        self.clients.append(client_id)

    def detect_issue(self, issue_id: int, description: str, resolution_steps: List[str]):
        issue = Issue(issue_id, description, resolution_steps, IssueStatus.DETECTED)
        self.issues.append(issue)
        self.notify_clients(issue)

    def resolve_issue(self, issue_id: int):
        for issue in self.issues:
            if issue.id == issue_id:
                issue.status = IssueStatus.RESOLVED
                self.notify_clients(issue)
                break

    def notify_clients(self, issue: Issue):
        notification = {
            "issue_id": issue.id,
            "description": issue.description,
            "resolution_steps": issue.resolution_steps,
            "status": issue.status.value
        }
        for client in self.clients:
            print(f"Sending notification to client {client}: {json.dumps(notification)}")

    def get_issue(self, issue_id: int):
        for issue in self.issues:
            if issue.id == issue_id:
                return issue
        return None
