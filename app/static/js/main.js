// Main JavaScript functionality

// Alert auto-close
document.addEventListener('DOMContentLoaded', function() {
    const alerts = document.querySelectorAll('.alert');
    alerts.forEach(alert => {
        setTimeout(() => {
            alert.style.display = 'none';
        }, 5000);
    });
});

// Form validation
function validateForm(formId) {
    const form = document.getElementById(formId);
    if (!form) return true;

    const inputs = form.querySelectorAll('input[required], textarea[required]');
    let isValid = true;

    inputs.forEach(input => {
        if (input.value.trim() === '') {
            input.style.borderColor = 'red';
            isValid = false;
        } else {
            input.style.borderColor = '';
        }
    });

    return isValid;
}

// Password strength checker
function checkPasswordStrength(password) {
    let strength = 0;
    
    if (password.length >= 8) strength++;
    if (/[a-z]/.test(password)) strength++;
    if (/[A-Z]/.test(password)) strength++;
    if (/[0-9]/.test(password)) strength++;
    if (/[^a-zA-Z0-9]/.test(password)) strength++;

    return strength;
}

// Confirmation dialogs
function confirmAction(message) {
    return confirm(message);
}

// Local storage utilities
const StorageUtil = {
    save: function(key, value) {
        localStorage.setItem(key, JSON.stringify(value));
    },
    get: function(key) {
        const item = localStorage.getItem(key);
        return item ? JSON.parse(item) : null;
    },
    remove: function(key) {
        localStorage.removeItem(key);
    },
    clear: function() {
        localStorage.clear();
    }
};

// Debounce function for API calls
function debounce(func, wait) {
    let timeout;
    return function executedFunction(...args) {
        const later = () => {
            clearTimeout(timeout);
            func(...args);
        };
        clearTimeout(timeout);
        timeout = setTimeout(later, wait);
    };
}

// Format time
function formatTime(seconds) {
    const minutes = Math.floor(seconds / 60);
    const secs = seconds % 60;
    return `${minutes}m ${secs}s`;
}

// Show loading spinner
function showLoading() {
    const spinner = document.createElement('div');
    spinner.className = 'loading-spinner';
    spinner.innerHTML = '<p>Loading...</p>';
    document.body.appendChild(spinner);
}

function hideLoading() {
    const spinner = document.querySelector('.loading-spinner');
    if (spinner) spinner.remove();
}

// API call helper
async function apiCall(url, options = {}) {
    try {
        const response = await fetch(url, {
            headers: {
                'Content-Type': 'application/json',
                ...options.headers
            },
            ...options
        });

        if (!response.ok) {
            throw new Error(`HTTP error! status: ${response.status}`);
        }

        return await response.json();
    } catch (error) {
        console.error('API call error:', error);
        throw error;
    }
}

// Smooth scroll
function smoothScroll(target) {
    const element = document.querySelector(target);
    if (element) {
        element.scrollIntoView({ behavior: 'smooth' });
    }
}

// Toggle visibility
function toggleVisibility(elementId) {
    const element = document.getElementById(elementId);
    if (element) {
        element.style.display = element.style.display === 'none' ? 'block' : 'none';
    }
}

// Keyboard shortcuts
document.addEventListener('keydown', function(event) {
    // ESC to dismiss modals
    if (event.key === 'Escape') {
        const modals = document.querySelectorAll('.modal');
        modals.forEach(modal => modal.style.display = 'none');
    }
});

// Print functionality
function printContent(elementId) {
    const element = document.getElementById(elementId);
    if (element) {
        const printWindow = window.open('', '', 'height=500,width=800');
        printWindow.document.write(element.innerHTML);
        printWindow.document.close();
        printWindow.print();
    }
}

console.log('Main JavaScript loaded successfully');
