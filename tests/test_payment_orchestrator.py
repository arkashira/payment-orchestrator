import pytest
from payment_orchestrator import PaymentOrchestrator, EmailTemplate, EmailTemplateType, Ticket

def test_add_email_template():
    orchestrator = PaymentOrchestrator()
    template = EmailTemplate(1, EmailTemplateType.ACKNOWLEDGEMENT, "Subject", "Body")
    orchestrator.add_email_template(template)
    assert len(orchestrator.email_templates) == 1

def test_add_ticket():
    orchestrator = PaymentOrchestrator()
    ticket = Ticket(1, "Open", [])
    orchestrator.add_ticket(ticket)
    assert len(orchestrator.tickets) == 1

def test_send_email():
    orchestrator = PaymentOrchestrator()
    template = EmailTemplate(1, EmailTemplateType.ACKNOWLEDGEMENT, "Subject", "Body")
    orchestrator.add_email_template(template)
    ticket = Ticket(1, "Open", [template])
    orchestrator.add_ticket(ticket)
    email_log = orchestrator.send_email(1, 1)
    assert email_log["template_id"] == 1

def test_send_email_template_not_found():
    orchestrator = PaymentOrchestrator()
    ticket = Ticket(1, "Open", [])
    orchestrator.add_ticket(ticket)
    with pytest.raises(ValueError):
        orchestrator.send_email(1, 1)

def test_send_email_ticket_not_found():
    orchestrator = PaymentOrchestrator()
    template = EmailTemplate(1, EmailTemplateType.ACKNOWLEDGEMENT, "Subject", "Body")
    orchestrator.add_email_template(template)
    with pytest.raises(ValueError):
        orchestrator.send_email(1, 1)

def test_get_email_logs():
    orchestrator = PaymentOrchestrator()
    template = EmailTemplate(1, EmailTemplateType.ACKNOWLEDGEMENT, "Subject", "Body")
    orchestrator.add_email_template(template)
    ticket = Ticket(1, "Open", [template])
    orchestrator.add_ticket(ticket)
    orchestrator.send_email(1, 1)
    email_logs = orchestrator.get_email_logs()
    assert len(email_logs) == 1

def test_update_email_template():
    orchestrator = PaymentOrchestrator()
    template = EmailTemplate(1, EmailTemplateType.ACKNOWLEDGEMENT, "Subject", "Body")
    orchestrator.add_email_template(template)
    orchestrator.update_email_template(1, "New Subject", "New Body")
    updated_template = orchestrator.email_templates[1]
    assert updated_template.subject == "New Subject"
    assert updated_template.body == "New Body"

def test_update_email_template_not_found():
    orchestrator = PaymentOrchestrator()
    with pytest.raises(ValueError):
        orchestrator.update_email_template(1, "New Subject", "New Body")
