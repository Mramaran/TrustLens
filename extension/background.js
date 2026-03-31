// Context Menu Creation
chrome.runtime.onInstalled.addListener(() => {
    chrome.contextMenus.create({
        id: "analyzeTrustLens",
        title: "Analyze with TrustLens",
        contexts: ["image"]
    });

    // Set up side panel
    chrome.sidePanel.setPanelBehavior({ openPanelOnActionClick: true });
});

// Handle Context Menu Click
chrome.contextMenus.onClicked.addListener((info, tab) => {
    if (info.menuItemId === "analyzeTrustLens") {
        const imageUrl = info.srcUrl;

        // Save URL/Image data to storage so popup can pick it up
        chrome.storage.local.set({ analyzableImage: imageUrl }, () => {
            // Open side panel
            chrome.sidePanel.open({ tabId: tab.id });
        });
    }
});
