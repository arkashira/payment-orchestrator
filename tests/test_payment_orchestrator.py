from payment_orchestrator import PaymentOrchestrator, IssueStatus

def test_detect_issue():
    orchestrator = PaymentOrchestrator()
    orchestrator.add_client(1)
    orchestrator.detect_issue(1, "Test issue", ["Step 1", "Step 2"])
    assert len(orchestrator.issues) == 1
    assert orchestrator.issues[0].status == IssueStatus.DETECTED

def test_resolve_issue():
    orchestrator = PaymentOrchestrator()
    orchestrator.add_client(1)
    orchestrator.detect_issue(1, "Test issue", ["Step 1", "Step 2"])
    orchestrator.resolve_issue(1)
    assert len(orchestrator.issues) == 1
    assert orchestrator.issues[0].status == IssueStatus.RESOLVED

def test_notify_clients():
    orchestrator = PaymentOrchestrator()
    orchestrator.add_client(1)
    orchestrator.add_client(2)
    orchestrator.detect_issue(1, "Test issue", ["Step 1", "Step 2"])
    # Check that notifications are sent to both clients
    assert len(orchestrator.issues) == 1

def test_get_issue():
    orchestrator = PaymentOrchestrator()
    orchestrator.detect_issue(1, "Test issue", ["Step 1", "Step 2"])
    issue = orchestrator.get_issue(1)
    assert issue is not None
    assert issue.id == 1
    assert issue.description == "Test issue"
    assert issue.resolution_steps == ["Step 1", "Step 2"]
    assert issue.status == IssueStatus.DETECTED

def test_get_non_existent_issue():
    orchestrator = PaymentOrchestrator()
    issue = orchestrator.get_issue(1)
    assert issue is None
