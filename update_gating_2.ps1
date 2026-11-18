$path = 'e:\AI_tutor\src\services\geminiWebSocket.ts'
$c = [System.IO.File]::ReadAllText($path)
$search = 'if (call.id && !this.executedToolCallIds.has(call.id)) {'
$replace = 'if (call.id && !this.executedToolCallIds.has(call.id) && this.pedagogicalStateManager.handleToolCall(call.name)) {'
$c = $c.Replace($search, $replace)
[System.IO.File]::WriteAllText($path, $c)
