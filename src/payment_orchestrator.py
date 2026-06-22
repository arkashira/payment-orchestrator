import json
from dataclasses import dataclass
from datetime import datetime
from enum import Enum
from typing import List, Dict

class EmailTemplateType(Enum):
    ACKNOWLEDGEMENT = 1
    IN_PROGRESS = 2
    RESOLVED = 3

@dataclass
class EmailTemplate:
    id: int
    type: EmailTemplateType
    subject: str
    body: str

@dataclass
class Ticket:
    id: int
    status: str
    email_templates: List[EmailTemplate]

class PaymentOrchestrator:
    def __init__(self):
        self.email_templates: Dict[int, EmailTemplate] = {}
        self.tickets: Dict[int, Ticket] = {}
        self.email_logs: List[Dict] = []

    def add_email_template(self, template: EmailTemplate):
        self.email_templates[template.id] = template

    def add_ticket(self, ticket: Ticket):
        self.tickets[ticket.id] = ticket

    def send_email(self, ticket_id: int, template_id: int):
        ticket = self.tickets.get(ticket_id)
        if ticket:
            template = self.email_templates.get(template_id)
            if template:
                email_log = {
                    "timestamp": datetime.now().isoformat(),
                    "template_id": template_id,
                    "success": True
                }
                self.email_logs.append(email_log)
                return email_log
            else:
                raise ValueError("Email template not found")
        else:
            raise ValueError("Ticket not found")

    def get_email_logs(self):
        return self.email_logs

    def update_email_template(self, template_id: int, subject: str, body: str):
        template = self.email_templates.get(template_id)
        if template:
            template.subject = subject
            template.body = body
        else:
            raise ValueError("Email template not found")
